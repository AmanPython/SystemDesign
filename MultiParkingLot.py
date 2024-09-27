class ParkingLot:
    def __init__(self, helper, parking):
        """
        Initialize the parking lot system with a helper for logging and a parking structure.
        """
        self.helper = helper
        self.parking = parking
        self.parked_vehicles = {}  # Maps spotId to (vehicleNumber, ticketId)

    def park(self, vehicle_type, vehicle_number, ticket_id):
        """
        Assign a parking spot to a vehicle based on the type and return the spot ID.
        """
        for i, floor in enumerate(self.parking):
            for j, row in enumerate(floor):
                for k, spot in enumerate(row):
                    if spot.startswith(f"{vehicle_type}-1"):
                        spot_id = f"{i}-{j}-{k}"
                        self.parking[i][j][k] = f"{vehicle_type}-0"  # Mark spot as taken
                        self.parked_vehicles[spot_id] = (vehicle_number, ticket_id)
                        return spot_id
        return ""

    def remove_vehicle(self, spot_id, vehicle_number, ticket_id):
        """
        Unpark or remove vehicle from parking spot.
        """
        if spot_id in self.parked_vehicles:
            del self.parked_vehicles[spot_id]
            floor, row, col = map(int, spot_id.split('-'))
            vehicle_type = self.parking[floor][row][col].split('-')[0]
            self.parking[floor][row][col] = f"{vehicle_type}-1"  # Mark spot as available
            return 201
        return 404

    def search_vehicle(self, spot_id, vehicle_number, ticket_id):
        """
        Search the vehicle parked using given identifiers.
        """
        for id, (v_number, t_id) in self.parked_vehicles.items():
            if vehicle_number == v_number or ticket_id == t_id:
                return id
        return ""

    def get_free_spots_count(self, floor, vehicle_type):
        """
        Get the count of free spots of a specific vehicle type on a specific floor.
        """
        count = 0
        for row in self.parking[floor]:
            count += sum(1 for spot in row if spot == f"{vehicle_type}-1")
        return count

class Helper:
    def print(self, message):
        print(message)

import unittest

class TestParkingLot(unittest.TestCase):
    def setUp(self):
        self.helper = Helper()
        self.parking = [
            [["4-1", "4-1", "2-1", "2-0"], 
             ["2-1", "4-1", "2-1", "2-1"], 
             ["4-0", "2-1", "4-0", "2-1"], 
             ["4-1", "4-1", "4-1", "2-1"]]
        ]
        self.lot = ParkingLot(self.helper, self.parking)

    def test_park_vehicle(self):
        spot_id = self.lot.park(4, "bh234", "tkt4534")
        self.assertNotEqual(spot_id, "")

    def test_remove_vehicle(self):
        spot_id = self.lot.park(4, "bh234", "tkt4534")
        status = self.lot.remove_vehicle(spot_id, "bh234", "tkt4534")
        self.assertEqual(status, 201)

    def test_search_vehicle(self):
        spot_id = self.lot.park(4, "xyz123", "ticket100")
        found_spot_id = self.lot.search_vehicle("", "xyz123", "")
        self.assertEqual(spot_id, found_spot_id)

    def test_get_free_spots_count(self):
        initial_count = self.lot.get_free_spots_count(0, 4)
        self.lot.park(4, "test123", "test_ticket")
        new_count = self.lot.get_free_spots_count(0, 4)
        self.assertEqual(initial_count - 1, new_count)

if __name__ == "__main__":
    unittest.main()
