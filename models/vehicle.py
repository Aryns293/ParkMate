from datetime import datetime

class Vehicle:
    def __init__(self, vehicle_number, driver_name, phone):
        self.vehicle_number = vehicle_number
        self.driver_name = driver_name
        self.phone = phone
        self.entry_time = datetime.now()

    def calculate_fare(self):
        duration = (datetime.now() - self.entry_time).total_seconds() / 3600
        duration = max(0.016, duration)
        return round(duration, 2)

class Car(Vehicle):
    rate_per_hour = 100

    def calculate_fare(self):
        hours = super().calculate_fare()
        return round(hours * self.rate_per_hour, 2)

class Bike(Vehicle):
    rate_per_hour = 50

    def calculate_fare(self):
        hours = super().calculate_fare()
        return round(hours * self.rate_per_hour, 2)
