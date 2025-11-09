class User:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)