# test_areas.py
import unittest
from areas import area_rectangle, area_circle, area_triangle


class TestAreas(unittest.TestCase):
     # Test case for a regular rectangle
    def test_area_rectangle_regular(self):
         # Test if the area of a rectangle with length 4 and width 5 is correct
        self.assertEqual(area_rectangle(4, 5), 20)
        
     # Test case for a square where length equals width
    def test_area_rectangle_square(self):
        # Test if the area of a square with side length 4 is correct
        self.assertEqual(area_rectangle(4, 4), 16)
        
    # Test case for a circle with radius 3
    def test_area_circle(self):
        # Test if the area of a circle with radius 3 is calculated correctly
        self.assertAlmostEqual(area_circle(3), 28.274, places=3)
        
    # Test case for a triangle with base 10 and height 5
    def test_area_triangle(self):
        self.assertEqual(area_triangle(10, 5), 25)
        
# This ensures the test cases run when this file is executed directly
if __name__ == "__main__":
    unittest.main()
