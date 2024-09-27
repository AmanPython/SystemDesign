class ParkingLot:
    def __init__(self, helper, parking):
        """
        Initialize the parking lot with multiple floors and designated spots for different vehicle types.
        Args:
            helper (Helper): A helper object for logging purposes.
            parking (list): A 3D list indicating the parking structure and spot types.
        """
        self.helper = helper
        self.parking = parking
        self.vehicle_info = {}  # Dictionary to map spotId to vehicle details

    def park(self, vehicleType, vehicleNumber, ticketId, parkingStrategy):
        """
        Park a vehicle in the parking lot based on the specified strategy.
        Args:
            vehicleType (int): The type of vehicle (2 for two-wheelers, 4 for four-wheelers).
            vehicleNumber (str): The vehicle's registration number.
            ticketId (str): A unique identifier for the parking ticket.
            parkingStrategy (int): The strategy for parking (0 for first-free, 1 for most-free).
        Returns:
            str: The spotId where the vehicle is parked or an empty string if no spot is available.
        """
        pass

    def removeVehicle(self, spotId):
        """
        Remove a vehicle from a specified spot.
        Args:
            spotId (str): The ID of the parking spot from which the vehicle is to be removed.
        Returns:
            bool: True if the vehicle is successfully removed, False otherwise.
        """
        pass

    def searchVehicle(self, query):
        """
        Search for a vehicle based on its number or ticket ID.
        Args:
            query (str): The vehicle number or ticket ID.
        Returns:
            str: The spotId of the vehicle if found, else an empty string.
        """
        pass

    def getFreeSpotsCount(self, floor, vehicleType):
        """
        Get the count of free spots for a specific vehicle type on a specified floor.
        Args:
            floor (int): The floor number.
            vehicleType (int): The vehicle type (2 or 4).
        Returns:
            int: Number of free spots available.
        """
        pass


class Helper:
    """
    A utility class to facilitate logging and other helper functionalities.
    """
    def print(self, message):
        print(message)

    def println(self, message):
        print(message + '\n')

import unittest

class TestParkingLot(unittest.TestCase):
    def setUp(self):
        helper = Helper()
        parking = [[
            [4, 4, 2, 2],
            [2, 4, 2, 0],
            [0, 2, 2, 2],
            [4, 4, 4, 0]
        ]]
        self.lot = ParkingLot(helper, parking)

    def test_park_vehicle(self):
        spot_id = self.lot.park(2, "BH234", "TKT4534", 0)
        self.assertEqual(spot_id, "0-0-2")

    def test_search_vehicle(self):
        self.lot.park(2, "BH234", "TKT4534", 0)
        spot_id = self.lot.searchVehicle("BH234")
        self.assertEqual(spot_id, "0-0-2")

    def test_remove_vehicle(self):
        spot_id = self.lot.park(2, "BH234", "TKT4534", 0)
        self.assertTrue(self.lot.removeVehicle(spot_id))

    def test_get_free_spots_count(self):
        self.lot.park(2, "BH234", "TKT4534", 0)
        count = self.lot.getFreeSpotsCount(0, 2)
        self.assertEqual(count, 6)

if __name__ == "__main__":
    unittest.main()
