from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import math
import database

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Campus center (example coordinates)
CAMPUS_LAT = 12.9716
CAMPUS_LON = 79.1590
RADIUS = 100


def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371000

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)

    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))

    return R*c


@app.get("/", response_class=HTMLResponse)
def student_page(request: Request):
    return templates.TemplateResponse("student.html", {"request": request})


@app.post("/mark_attendance")
async def mark_attendance(request: Request):

    data = await request.json()

    name = data["name"]
    lat = float(data["lat"])
    lon = float(data["lon"])

    client_ip = request.client.host

    # IP restriction (50 minutes)
    database.cursor.execute(
        """
        SELECT * FROM attendance
        WHERE ip=? AND timestamp >= datetime('now','-50 minutes')
        """,
        (client_ip,)
    )

    existing = database.cursor.fetchone()

    if existing:
        return {
            "status": "Rejected",
            "message": "IP already used within 50 minutes"
        }

    distance = calculate_distance(CAMPUS_LAT, CAMPUS_LON, lat, lon)

    status = "ON CAMPUS"

    if distance > RADIUS:
        status = "LEFT CAMPUS ⚠"

    database.cursor.execute(
        "INSERT INTO attendance (name, latitude, longitude, ip, status) VALUES (?, ?, ?, ?, ?)",
        (name, lat, lon, client_ip, status)
    )

    database.conn.commit()

    return {
        "message": "Attendance recorded",
        "status": status,
        "ip": client_ip
    }


@app.post("/update_location")
async def update_location(request: Request):

    data = await request.json()

    name = data["name"]
    lat = float(data["lat"])
    lon = float(data["lon"])

    distance = calculate_distance(CAMPUS_LAT, CAMPUS_LON, lat, lon)

    status = "ON CAMPUS"

    if distance > RADIUS:
        status = "LEFT CAMPUS ⚠"

    database.cursor.execute(
        "UPDATE attendance SET latitude=?, longitude=?, status=? WHERE name=?",
        (lat, lon, status, name)
    )

    database.conn.commit()

    return {"status": status}


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):

    database.cursor.execute("SELECT * FROM attendance")
    data = database.cursor.fetchall()

    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request, "data": data}
    )