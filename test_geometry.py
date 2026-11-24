import unittest

import circle
import square
import rectangle


class CircleTestCase(unittest.TestCase):
    def test_area_normal(self):
        self.assertAlmostEqual(circle.area(2), 12.566370614359172)

    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_area_fractional(self):
        self.assertAlmostEqual(circle.area(0.5), 0.7853981633974483)

    def test_perimeter_normal(self):
        self.assertAlmostEqual(circle.perimeter(3), 18.84955592153876)

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_fractional(self):
        self.assertAlmostEqual(circle.perimeter(0.5), 3.141592653589793)


class SquareTestCase(unittest.TestCase):
    def test_area_normal(self):
        self.assertEqual(square.area(4), 16)

    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_area_fractional(self):
        self.assertAlmostEqual(square.area(1.5), 2.25)

    def test_perimeter_normal(self):
        self.assertEqual(square.perimeter(4), 16)

    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_fractional(self):
        self.assertAlmostEqual(square.perimeter(1.5), 6)


class RectangleTestCase(unittest.TestCase):
    def test_area_normal(self):
        self.assertEqual(rectangle.area(3, 5), 15)

    def test_area_zero(self):
        self.assertEqual(rectangle.area(10, 0), 0)

    def test_area_square(self):
        self.assertEqual(rectangle.area(10, 10), 100)

    def test_area_fractional(self):
        self.assertAlmostEqual(rectangle.area(1.5, 2.5), 3.75)

    def test_perimeter_normal(self):
        self.assertEqual(rectangle.perimeter(3, 5), 16)

    def test_perimeter_zero(self):
        self.assertEqual(rectangle.perimeter(0, 5), 10)

    def test_perimeter_square(self):
        self.assertEqual(rectangle.perimeter(10, 10), 40)

    def test_perimeter_fractional(self):
        self.assertAlmostEqual(rectangle.perimeter(1.5, 2.5), 8)


if __name__ == '__main__':
    unittest.main()
