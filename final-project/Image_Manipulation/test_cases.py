from re import L
import unittest
from solutions import *
from image import Image
import numpy as np
import random
import cv2

#For test cases, please pass in the images that are in the 
#test_case_input. We will specify which image to test!

#The test_images folder should be inside input for this to work. Please don't move around the images!!

#FOR TEST CASES YOU WILL NEED TO MAKE AN EDIT IN THE IMAGE.PY FILE:
#Make self.output_path = 'input/test_images/'
#Once you are done testing the files please change it back to self.output_path = 'output'
#this will make sure your files will end up where they're supposed to :))



class Test_Image_Manipulation(unittest.TestCase):
    def test_brightness(self):
        student_answer=0
        image1 = Image(filename="test_images/Sunflower.png")
        image=brighten(image1,2)
        image.write_image("bright_function.png")
        
        test = cv2.imread("input/test_images/bright.png")
        students = cv2.imread("output/bright_function.png")
        
        if not (test.shape == students.shape):
            student_answer=3
        difference = cv2.subtract(test, students)
        b, g, r = cv2.split(difference)
        if not(cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0):
            student_answer=3

        self.assertEqual(0,student_answer)
    
    def test_dimming(self):
        student_answer=0
        image1 = Image(filename="test_images/Sunflower.png")
        image=brighten(image1,0.5)
        image.write_image("dim_function.png")
        
        test = cv2.imread("input/test_images/dim.png")
        students = cv2.imread("output/dim_function.png")
        
        if not (test.shape == students.shape):
            student_answer=3
        difference = cv2.subtract(test, students)
        b, g, r = cv2.split(difference)
        if not(cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0):
            student_answer=3

        self.assertEqual(0,student_answer)
    
    def test_high_contrast(self):
        student_answer=0
        image1 = Image(filename="test_images/Sunflower.png")
        image=adjust_contrast(image1,2,0.5)
        image.write_image("high_contrast_function.png")
        
        test = cv2.imread("input/test_images/high_contrast.png")
        students = cv2.imread("output/high_contrast_function.png")
        
        if not (test.shape == students.shape):
            student_answer=3
        difference = cv2.subtract(test, students)
        b, g, r = cv2.split(difference)
        if not(cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0):
            student_answer=3

        self.assertEqual(0,student_answer)
    
    def test_low_contrast(self):
        student_answer=0
        image1 = Image(filename="test_images/Sunflower.png")
        image=adjust_contrast(image1,0.3,0.5)
        image.write_image("low_contrast_function.png")
        
        test = cv2.imread("input/test_images/low_contrast.png")
        students = cv2.imread("output/test_images/low_contrast_function.png")
        
        if not (test.shape == students.shape):
            student_answer=3
        difference = cv2.subtract(test, students)
        b, g, r = cv2.split(difference)
        if not(cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0):
            student_answer=3

        self.assertEqual(0,student_answer)
    
    def test_blur(self):
        student_answer=0
        image1 = Image(filename="test_images/Sunflower.png")
        image=blur(image1,13)
        image.write_image("blur_function.png")
        
        test = cv2.imread("input/test_images/blur.png")
        students = cv2.imread("output/blur_function.png")
        
        if not (test.shape == students.shape):
            student_answer=3
        difference = cv2.subtract(test, students)
        b, g, r = cv2.split(difference)
        if not(cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0):
            student_answer=3

        self.assertEqual(0,student_answer)
    
    
    def test_apply_kernel_y(self):
        y_edge=np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
        student_answer=0
        image1 = Image(filename="test_images/city.png")
        image=apply_kernel(image1,y_edge)
        image.write_image("apply_kernel_y_function.png")
        
        test = cv2.imread("input/test_images/apply_kernel_y.png")
        students = cv2.imread("output/apply_kernel_y_function.png")
        
        if not (test.shape == students.shape):
            student_answer=3
        difference = cv2.subtract(test, students)
        b, g, r = cv2.split(difference)
        if not(cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0):
            student_answer=3

        self.assertEqual(0,student_answer)
    
    def test_apply_kernel_x(self):
        x_edge=np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
        student_answer=0
        image1 = Image(filename="test_images/city.png")
        image=apply_kernel(image1,x_edge)
        image.write_image("apply_kernel_x_function.png")
        
        test = cv2.imread("input/test_images/apply_kernel_x.png")
        students = cv2.imread("output/apply_kernel_x_function.png")
        
        if not (test.shape == students.shape):
            student_answer=3
        difference = cv2.subtract(test, students)
        b, g, r = cv2.split(difference)
        if not(cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0):
            student_answer=3

        self.assertEqual(0,student_answer)
 
    def test_combine_kernel(self):
        student_answer=0
        image1 = Image(filename="test_images/apply_kernel_x.png")
        image2 = Image(filename="test_images/apply_kernel_y.png")
        image=combine_images(image1,image2)
        image.write_image("combine_function.png")
        
        test = cv2.imread("input/test_images/combine.png")
        students = cv2.imread("output/combine_function.png")
        
        if not (test.shape == students.shape):
            student_answer=3
        difference = cv2.subtract(test, students)
        b, g, r = cv2.split(difference)
        if not(cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0):
            student_answer=3

        self.assertEqual(0,student_answer, "This might not work if one of test_apply kernel fails")
     
    def test_combine(self):
        student_answer=0
        image1 = Image(filename="test_images/cake.png")
        image2 = Image(filename="test_images/brownie.png")
        image=combine_images(image1,image2)
        image.write_image("combine_function2.png")
        
        test = cv2.imread("input/test_images/combine_again.png")
        students = cv2.imread("output/combine_function2.png")
        
        if not (test.shape == students.shape):
            student_answer=3
        difference = cv2.subtract(test, students)
        b, g, r = cv2.split(difference)
        if not(cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0):
            student_answer=3

        self.assertEqual(0,student_answer)
    
    def test_invert(self):
        student_answer=0
        image1 = Image(filename="test_images/Sunflower.png")
        image=invert_image(image1)
        image.write_image("invert_function.png")
        
        test = cv2.imread("input/test_images/invert.png")
        students = cv2.imread("output/invert_function.png")
        
        if not (test.shape == students.shape):
            student_answer=3
        difference = cv2.subtract(test, students)
        b, g, r = cv2.split(difference)
        if not(cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0):
            student_answer=3

        self.assertEqual(0,student_answer)

    def test_create_border(self):
        student_answer=0
        image1 = Image(filename="test_images/city.png")
        image2 = Image(filename="test_images/Sunflower.png")
        image=create_a_border(image1,image2,[0,0],[30,30])
        image.write_image("border_function.png")
        
        test = cv2.imread("input/test_images/border.png")
        students = cv2.imread("output/border_function.png")
        
        if not (test.shape == students.shape):
            student_answer=3
        difference = cv2.subtract(test, students)
        b, g, r = cv2.split(difference)
        if not(cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0):
            student_answer=3

        self.assertEqual(0,student_answer)
    

    
        
if __name__ == "__main__":
    unittest.main()