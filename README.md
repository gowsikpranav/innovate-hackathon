# innovate-hackathon
# Smart Attendance Integrity System

## Overview

The Smart Attendance Integrity System is a geofence-based attendance platform designed to prevent students from marking attendance and leaving campus immediately. The system integrates GPS location verification, IP tracking, and real-time monitoring to ensure authentic student presence.

This solution improves the reliability of attendance systems used in educational institutions by combining **digital verification with location-based monitoring**.

---

# Problem Statement

Traditional attendance systems (especially biometric or manual attendance) allow students to mark attendance and leave the campus immediately. This leads to:

* False attendance records
* Difficulty for faculty in monitoring student presence
* Reduced classroom participation
* Administrative inefficiencies

---

# Proposed Solution

This project introduces a **location-aware attendance system** that verifies whether a student remains within the campus geofence after marking attendance.

The system includes:

* GPS-based geofencing
* IP address tracking
* Attendance validation
* Real-time location monitoring
* Faculty dashboard

---

# Key Features

# Geofenced Attendance

Attendance is verified based on whether the student is within a predefined campus radius.

### IP Verification

The system records the student's IP address and restricts multiple attendance entries from the same IP within a specified time window.

### Live Location Tracking

After marking attendance, the student's location is updated periodically to ensure they remain on campus.

### Faculty Dashboard

Faculty can monitor student attendance records including:

* Student name
* Location coordinates
* IP address
* Attendance status
* Timestamp

### Proxy Attendance Prevention

The system blocks attendance attempts from the same IP address within **50 minutes**, preventing proxy attendance.

---

# System Architecture

Student Device (Browser)
↓
GPS Location + Name
↓
FastAPI Backend Server
↓
Geofence & IP Validation
↓
SQLite Database
↓
Faculty Dashboard

---

# Technology Stack

Frontend

* HTML
* CSS (Bootstrap)
* JavaScript

Backend

* FastAPI (Python)

Database

* SQLite

Other Technologies

* Geolocation API
* Geofencing Logic

---

# Project Structure

```
attendance_system
│
├── main.py
├── database.py
│
├── templates
│   ├── student.html
│   └── dashboard.html
│
└── static
    └── script.js
```

---

# Installation

Clone the repository:

```
git clone https://github.com/yourusername/attendance-system.git
```

Navigate to the project folder:

```
cd attendance-system
```

Install dependencies:

```
pip install fastapi uvicorn jinja2 python-multipart
```

Run the server:

```
uvicorn main:app --reload
```

---

# Usage

Open the student interface:

```
http://127.0.0.1:8000
```

Students can mark attendance by entering their name and allowing location access.

Open the faculty dashboard:

```
http://127.0.0.1:8000/dashboard
```

The dashboard displays real-time attendance information.

---

# Future Improvements

* QR code-based classroom verification
* Face recognition for identity validation
* Real-time campus map visualization
* Integration with biometric attendance systems
* AI-based anomaly detection

---

# Authors
Gowaik V
Sai Deepthi P
Lakshaya R
---

# License

This project is developed for academic and hackathon purposes.

