from models.parking_lot import ParkingLot
from models.vehicle import Car, Bike
from services.db_service import DBService

class ParkingManager:
    def __init__(self, total_slots):
        self.lot = ParkingLot(total_slots)
        self.parked_vehicles = {}
        self.db = DBService()

    def park_vehicle(self, vehicle_number, vehicle_type, driver_name, phone):
        slot = self.lot.get_random_free_slot()
        if slot is None:
            return None

        vehicle = Car(vehicle_number, driver_name, phone) if vehicle_type.lower() == "car" else Bike(vehicle_number, driver_name, phone)
        slot.park(vehicle)
        self.parked_vehicles[vehicle_number] = slot.slot_id
        return slot.slot_id

    def leave_slot(self, slot_id):
        slot = next((s for s in self.lot.slots if s.slot_id == slot_id), None)
        if slot and slot.is_occupied:
            vehicle = slot.leave()
            fare = vehicle.calculate_fare()
            self.db.add_history(vehicle, fare)
            for k, v in list(self.parked_vehicles.items()):
                if v == slot_id:
                    del self.parked_vehicles[k]
                    break
            return fare, vehicle
        return 0, None

    def get_all_slots(self):
        return self.lot.get_all_slots()
