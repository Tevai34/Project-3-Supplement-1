# test_areas.py
import unittest
from test_areas import area_rectangle, area_circle, area_triangle

class TestAreas(unittest.TestCase):
    def test_area_rectangle_regular(self):
        self.assertEqual(area_rectangle(4, 5), 20)

    def test_area_rectangle_square(self):
        self.assertEqual(area_rectangle(4, 4), 16)

    def test_area_circle(self):
        self.assertAlmostEqual(area_circle(3), 28.274, places=3)

    def test_area_triangle(self):
        self.assertEqual(area_triangle(10, 5), 25)

if __name__ == "__main__":
    unittest.main()
