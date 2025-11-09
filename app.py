from flask import Flask, render_template, request, redirect, url_for, flash
from services.parking_service import ParkingManager
from services.metrics_service import MetricsService

app = Flask(__name__)
app.secret_key = "supersecretkey"

manager = ParkingManager(total_slots=10)
metrics = MetricsService()

@app.route("/")
def index():
    stats = metrics.calculate_system_metrics()
    return render_template("index.html", slots=manager.get_all_slots(), stats=stats)

@app.route("/park", methods=["POST"])
def park_vehicle():
    vehicle_number = request.form.get("vehicle_number")
    vehicle_type = request.form.get("vehicle_type")
    driver_name = request.form.get("driver_name")
    phone = request.form.get("phone")

    slot = manager.park_vehicle(vehicle_number, vehicle_type, driver_name, phone)

    if slot is None:
        flash("🚫 No Space in Parking Slot!")
    return redirect(url_for('index'))

@app.route("/leave/<int:slot_id>")
def leave_slot(slot_id):
    fare, vehicle = manager.leave_slot(slot_id)
    if vehicle:
        flash(f"💰 Vehicle {vehicle.vehicle_number} ({vehicle.driver_name}) Fare: ₹{fare}")
    return redirect(url_for('index'))

@app.route("/history")
def history():
    history_data = metrics.get_parking_history()
    return render_template("history.html", records=history_data)

if __name__ == "__main__":
    app.run(debug=True)
