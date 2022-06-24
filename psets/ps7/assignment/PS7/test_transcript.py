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

    def test_course_str_science_honors(self):
        string = Honors('Science Honors', 85, 12).__str__()
        self.assertIn('Science Honors', string)
        self.assertIn('B', string)

    def test_course_str_ap_english(self):
        string = AP('AP English', 73, 12).__str__()
        self.assertIn('AP English', string)
        self.assertIn('C-', string)

    # lettergrades

    def test_course_letter_grade_chemistry(self):
        chemistry = Course("Chemistry", 91, 12)
        grade = chemistry.letter_grade()
        self.assertEqual(grade, 'A-', "Check your Course's letter_grade function! A 91 should map to an A-")

    def test_course_letter_grade_ap_physics(self):
        ap_physics = AP("AP Physics", 53, 12)
        grade = ap_physics.letter_grade()
        self.assertEqual(grade, 'F', "Check your AP's letter_grade function! A 53 should map to a F")

    def test_course_letter_grade_psychology(self):
        psychology = Course("Psychology", 89, 12)
        grade = psychology.letter_grade()
        self.assertEqual(grade, 'B+', "Check your Course's letter_grade function! An 89 should map to a B+")

    def test_course_letter_grade_honors_literature(self):
        honors_lit = Honors("Honors Literature", 66, 12)
        grade = honors_lit.letter_grade()
        self.assertEqual(grade, 'D', "Check your Honors letter_grade function! A 66 should map to a D")

    # grade_point() methods

    def test_course_grade_point_chemistry(self):
        chemistry = Course("Chemistry", 91, 12)
        gpa = chemistry.grade_point()
        self.assertEqual(gpa, 3.7, "Check your Course's grade_point function! A 91 should result in a 3.7 gpa")

    def test_course_grade_point_ap_physics(self):
        ap_physics = AP("AP Physics", 53, 12)
        gpa = ap_physics.grade_point()
        self.assertEqual(gpa, 1.0, "Check your AP's grade_point function! An AP 53 should result in a 1.0 gpa")

    def test_course_grade_point_psychology(self):
        psychology = Course("Psychology", 89, 12)
        gpa = psychology.grade_point()
        self.assertEqual(gpa, 3.3, "Check your Course's grade_point function! An 89 should result in a 3.3 gpa")

    def test_course_grade_pointh_honors_literature(self):
        honors_lit = Honors("Honors Literature", 66, 12)
        gpa = honors_lit.grade_point()
        self.assertEqual(gpa, 1.5, "Check your Honors grade_point function! An Honors 66 should result in a 1.5 gpa")

    def test_course_grade_point_math_A(self):
        math = Course("Math", 99, 12)
        gpa = math.grade_point()
        self.assertEqual(gpa, 4.0, "Check your Course grade_point function! A 99 should result in a 4.0 gpa")

    def test_course_grade_point_spanish_D(self):
        spanish = Course("Spanish", 60, 12)
        gpa = spanish.grade_point()
        self.assertEqual(gpa, 0.7, "Check your Course grade_point function! A 60 should result in a 0.7 gpa")

    def test_course_grade_point_science_honors(self):
        science = Honors("Science Honors", 85, 12)
        gpa = science.grade_point()
        self.assertEqual(gpa, 3.5, "Check your Honors letter_grade function! An Honors 85 should result in a 3.5 gpa")

    def test_course_grade_point_ap_english(self):
        ap_english = AP('AP English', 73, 12)
        gpa = ap_english.grade_point()
        self.assertEqual(gpa, 2.7, "Check your AP letter_grade function! An AP 73 should result in a 2.7 gpa")


if __name__ == "__main__":
    unittest.main()
