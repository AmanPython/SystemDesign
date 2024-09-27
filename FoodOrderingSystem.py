class FoodOrderingSystem:
    def __init__(self, helper):
        """
        Initialize the food ordering system with a helper for logging.
        """
        self.helper = helper
        self.orders = {}
        self.restaurants = {}
        self.food_items = {}
        self.restaurant_ratings = {}
        self.food_item_ratings = {}

    def orderFood(self, orderId, restaurantId, foodItemId):
        """
        Place an order for a food item from a specified restaurant.
        """
        pass

    def rateOrder(self, orderId, rating):
        """
        Rate a given order, affecting both the food item and the restaurant's overall rating.
        """
        pass

    def getTopRestaurantsByFood(self, foodItemId):
        """
        Return a list of the top 20 restaurants for a specific food item, based on ratings.
        """
        pass

    def getTopRatedRestaurants(self):
        """
        Return a list of the top 20 restaurants based on overall ratings.
        """
        pass

class Helper:
    def print(self, message):
        print(message)



import unittest

class TestFoodOrderingSystem(unittest.TestCase):
    def setUp(self):
        self.helper = Helper()
        self.system = FoodOrderingSystem(self.helper)

    def test_order_and_rate_food(self):
        self.system.orderFood("order-1", "restaurant-1", "food-1")
        self.system.rateOrder("order-1", 5)
        self.assertEqual(self.system.food_item_ratings["food-1"]["restaurant-1"], 5)
        self.assertEqual(self.system.restaurant_ratings["restaurant-1"], 5)

    def test_get_top_restaurants_by_food(self):
        # Setup multiple orders and ratings
        self.system.orderFood("order-1", "restaurant-1", "food-1")
        self.system.rateOrder("order-1", 5)
        self.system.orderFood("order-2", "restaurant-2", "food-1")
        self.system.rateOrder("order-2", 4)
        top_restaurants = self.system.getTopRestaurantsByFood("food-1")
        self.assertEqual(top_restaurants[0], "restaurant-1")
        self.assertEqual(top_restaurants[1], "restaurant-2")

    def test_get_top_rated_restaurants(self):
        # Setup multiple orders and ratings across different restaurants
        self.system.orderFood("order-3", "restaurant-3", "food-2")
        self.system.rateOrder("order-3", 3)
        self.system.orderFood("order-4", "restaurant-4", "food-3")
        self.system.rateOrder("order-4", 4)
        top_rated_restaurants = self.system.getTopRatedRestaurants()
        self.assertEqual(top_rated_restaurants[0], "restaurant-4")
        self.assertEqual(top_rated_restaurants[1], "restaurant-3")

if __name__ == "__main__":
    unittest.main()
