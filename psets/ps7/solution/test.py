import unittest

from transcript import *


class TestTranscript(unittest.TestCase):
    def test_course_str_math_A(self):
        string = Course('Math', 99, 12).__str__()
        self.assertIn('Math', string)
        self.assertIn('A+', string)

    def test_course_str_spanish_D(self):
        string = Course('Spanish', 60, 12).__str__()
        self.assertIn('Spanish', string)
        self.assertIn('D-', string)

    # TODO: add similar test cases for honors, ap

    # TODO: add similar test cases for letter_grade() and grade_point() methods
    # for Course, Honors, and AP


class TestShape(unittest.TestCase):
    # TODO write tests for shape.py
    pass


if __name__ == "__main__":
    unittest.main()
