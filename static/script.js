function markAttendance() {

let name = document.getElementById("name").value.trim();
let resultBox = document.getElementById("result");

if(name === ""){
resultBox.innerHTML = "<span style='color:red'>⚠ Please enter your name</span>";
return;
}

resultBox.innerHTML = "📍 Getting your location...";

if(!navigator.geolocation){
resultBox.innerHTML = "<span style='color:red'>Geolocation not supported</span>";
return;
}

navigator.geolocation.getCurrentPosition(function(position){

let lat = position.coords.latitude;
let lon = position.coords.longitude;

resultBox.innerHTML = "⏳ Recording attendance...";

fetch("/mark_attendance",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
name:name,
lat:lat,
lon:lon
})

})
.then(response => response.json())
.then(data => {

if(data.status === "Rejected"){
resultBox.innerHTML =
"<span style='color:red'>❌ " + data.message + "</span>";
return;
}

resultBox.innerHTML =
"<div style='color:green;font-weight:bold'>✅ Attendance Recorded</div>" +
"<div>Status: " + data.status + "</div>" +
"<div>IP: " + data.ip + "</div>";

startTracking(name);

})
.catch(error => {

resultBox.innerHTML =
"<span style='color:red'>Server error. Try again.</span>";

console.error(error);

});

},
function(error){

resultBox.innerHTML =
"<span style='color:red'>⚠ Location access denied</span>";

});

}


function startTracking(name){

setInterval(function(){

navigator.geolocation.getCurrentPosition(function(position){

let lat = position.coords.latitude;
let lon = position.coords.longitude;

fetch("/update_location",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
name:name,
lat:lat,
lon:lon
})

})
.then(response => response.json())
.then(data => {

console.log("Location updated:", data.status);

})
.catch(error => {

console.log("Tracking error:", error);

});

});

},120000); // every 2 minutes

}