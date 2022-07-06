from re import L
import unittest
from Day_1 import *
from image import Image
import numpy as np
import random

#For test cases, please pass in the images that are in the 
#test_case_input. We will specify which image to test!

#The test_images folder should be inside input for this to work



class Test_Image_Manipulation(unittest.TestCase):
    def test_brightness(self):
        image1 = Image(filename="test_images/Sunflower.png")

        image=brighten(image1,2)
 
        

        brightenImage=Image(filename="test_images/bright.png")
        for i in range(image.array.shape[0]):
            for j in range(image.array.shape[1]):
                for k in range(image.array.shape[2]):
                    self.assertEqual((brightenImage.array[i][j][k]),((image.array[i][j][k],1)))
   
        
if __name__ == "__main__":
    unittest.main()