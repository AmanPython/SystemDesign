class WebpageVisitsCounter:
    def __init__(self, totalPages, helper):
        """
        Initialize the counter with the total number of pages and a helper for logging.
        Args:
            totalPages (int): Total number of webpages.
            helper (Helper): Helper object for logging.
        """
        self.totalPages = totalPages
        self.visitCounts = [0] * totalPages
        self.helper = helper

    def incrementVisitCount(self, pageIndex):
        """
        Increment the visit count for a specific webpage.
        Args:
            pageIndex (int): Index of the webpage to increment.
        """
        if pageIndex < self.totalPages:
            self.visitCounts[pageIndex] += 1
            self.helper.print(f"Incremented visit count for page {pageIndex}: {self.visitCounts[pageIndex]}")
        else:
            self.helper.print("Invalid page index")

    def getVisitCount(self, pageIndex):
        """
        Get the total visit count for a specific webpage.
        Args:
            pageIndex (int): Index of the webpage.
        Returns:
            int: Visit count of the webpage.
        """
        if pageIndex < self.totalPages:
            return self.visitCounts[pageIndex]
        else:
            self.helper.print("Invalid page index")
            return -1

class Helper:
    def print(self, message):
        print(message)

# Unit Testing
import unittest

class TestWebpageVisitsCounter(unittest.TestCase):
    def setUp(self):
        self.helper = Helper()
        self.counter = WebpageVisitsCounter(1000, self.helper)

    def test_increment_and_get_visit_count(self):
        # Simulate visits
        self.counter.incrementVisitCount(10)
        self.counter.incrementVisitCount(10)
        self.counter.incrementVisitCount(20)
        
        # Check visit counts
        self.assertEqual(self.counter.getVisitCount(10), 2)
        self.assertEqual(self.counter.getVisitCount(20), 1)
        self.assertEqual(self.counter.getVisitCount(15), 0)  # Check for page with no visits

    def test_invalid_page_index(self):
        # Attempt to access a page index that does not exist
        with self.assertRaises(IndexError):
            self.counter.incrementVisitCount(1001)
        
        # Attempt to get visit count for an invalid page
        self.assertEqual(self.counter.getVisitCount(1001), -1)

if __name__ == "__main__":
    unittest.main()
