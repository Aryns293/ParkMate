import random

class ParkingSlot:
    def __init__(self, slot_id):
        self.slot_id = slot_id
        self.is_occupied = False
        self.vehicle = None

    def park(self, vehicle):
        if not self.is_occupied:
            self.vehicle = vehicle
            self.is_occupied = True
            return True
        return False

    def leave(self):
        v = self.vehicle
        self.vehicle = None
        self.is_occupied = False
        return v


class ParkingLot:
    def __init__(self, total_slots=10):
        self.slots = [ParkingSlot(i+1) for i in range(total_slots)]

    def get_random_free_slot(self):
        free_slots = [slot for slot in self.slots if not slot.is_occupied]
        if not free_slots:
            return None
        return random.choice(free_slots)

    def get_all_slots(self):
        return self.slots