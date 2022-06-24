from cmath import pi
import unittest

from shape import *


class TestShape(unittest.TestCase):

    def test_rect_area(self):
        rect = Rectangle(2, 4)
        rect_area = rect.find_area()
        self.assertEqual(rect_area, 8, "The area of a 2x4 rectangle should be 8. Check your rectangle area function!")

    def test_rect_perimeter(self):
        rect = Rectangle(2, 4)
        rect_perimeter = rect.find_perimeter()
        self.assertEqual(rect_perimeter, 12,
                         "The perimeter of a 2x4 rectangle should be 12. Check your rectangle perimeter function!")

    def test_square_area(self):
        square = Square(2)
        square_area = square.find_area()
        self.assertEqual(square_area, 4, "The area of a 2x2 square should be 4. Check your square area function!")

    def test_square_perimeter(self):
        square = Square(2)
        square_perimeter = square.find_perimeter()
        self.assertEqual(square_perimeter, 8,
                         "The perimeter of a 2x2 square should be 8. Check your square perimeter function!")

    def test_circle_area(self):
        circle = Circle(4)
        circle_area = circle.find_area()
        self.assertEqual(
            circle_area, 4*4*pi, "The area of a circle w/ a radius of 4 should be approximately 50.24. Check your circle area function!")

    def test_cirlce_perimeter(self):
        circle = Circle(4)
        circle_perimeter = circle.find_perimeter()
        self.assertEqual(circle_perimeter, 8*pi,
                         "The perimeter of a circle w/ a radius of 4 should be approximately 25.12. Check your circle perimeter function!")

    def test_triangle_area(self):
        triangle = Triangle(2, 5)
        triangle_area = triangle.find_area()
        self.assertEqual(
            triangle_area, 5, "The area of a triangle w/ a base of 2 and height of 5 should be 5. Check your triangle area function!")


if __name__ == "__main__":
    unittest.main()
