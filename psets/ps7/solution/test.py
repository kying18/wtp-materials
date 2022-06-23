from cmath import pi
import unittest

from transcript import *

from pets import *

from shape import *

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

    #lettergrades

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
  
    #grade_point() methods

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
    
class TestShape(unittest.TestCase):
    
    def test_rect_area(self):
        rect=Rectangle(2,4)
        rect_area=rect.find_area()
        self.assertEqual(rect_area,8,"The area of a 2x4 rectangle should be 8. Check your rectangle area function!")
    
    def test_rect_perimeter(self):
        rect=Rectangle(2,4)
        rect_perimeter=rect.find_perimeter()
        self.assertEqual(rect_perimeter,12,"The perimeter of a 2x4 rectangle should be 12. Check your rectangle perimeter function!")
    
    def test_square_area(self):
        square=Square(2)
        square_area=square.find_area()
        self.assertEqual(square_area,4,"The area of a 2x2 square should be 4. Check your square area function!")

    def test_square_perimeter(self):
        square=Square(2)
        square_perimeter=square.find_perimeter()
        self.assertEqual(square_perimeter,8,"The perimeter of a 2x2 square should be 8. Check your square perimeter function!")
        
    def test_circle_area(self):
        circle=Circle(4)
        circle_area=circle.find_area()
        self.assertEqual(circle_area,4*4*pi,"The area of a circle w/ a radius of 4 should be approximately 50.24. Check your circle area function!")

    def test_cirlce_perimeter(self):
        circle=Circle(4)
        circle_perimeter=circle.find_perimeter()
        self.assertEqual(circle_perimeter,8*pi,"The perimeter of a circle w/ a radius of 4 should be approximately 25.12. Check your circle perimeter function!")

    def test_triangle_area(self):
        triangle=Triangle(2,5)
        triangle_area=triangle.find_area()
        self.assertEqual(triangle_area,5,"The area of a triangle w/ a base of 2 and height of 5 should be 5. Check your triangle area function!")


# NOTE TO STUDENTS: this is for the optional question
class TestPets(unittest.TestCase):
    def test_cat_speak(self):
        cat1=Cat("cat")
        self.assertEqual((cat1.speak()).lower(),"meow","Cat should say meow when speaking!")

    def test_dog_speak(self):
        dog1=Dog("dog1",False)
        self.assertEqual(dog1.speak(),"bark","Make sure your quiet dog is able to say 'bark'!")
    
    def test_dog_speak_loud(self):
        dog2=Dog("dog2",True)
        self.assertEqual(dog2.speak(),"BARK","Make sure the loud dog is able to say 'BARK'")


if __name__ == "__main__":
    unittest.main()
