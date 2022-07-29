"""
Python Image Manipulation Empty Template by Kylie Ying (modified from MIT 6.865)
YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

from re import S
from image import Image
import numpy as np
import random

def brighten(image, factor):
    # when we brighten, we just want to make each channel higher by some amount 
    # factor is a value > 0, how much you want to brighten the image by (< 1 = darken, > 1 = brighten)
    pass

def adjust_contrast(image, factor, mid):
    # adjust the contrast by increasing the difference from the user-defined midpoint by factor amount
    pass

def blur(image, kernel_size):
    # kernel size is the number of pixels to take into account when applying the blur
    # (ie kernel_size = 3 would be neighbors to the left/right, top/bottom, and diagonals)
    pass

def apply_kernel(image, kernel):
    # the kernel should be a 2D array that represents the kernel we'll use!
    # for the sake of simiplicity of this implementation, let's assume that the kernel is SQUARE
    # for example the sobel x kernel (detecting horizontal edges) is as follows:
    # [1 0 -1]
    # [2 0 -2]
    # [1 0 -1]
    pass

def motion_blur(image,kernel_size):
    #makes an object look like it's moving either in horizontal  or vertical direction
    pass

def combine_images(image1, image2):
    # let's combine two images using the squared sum of squares: value = sqrt(value_1**2, value_2**2)
    # size of image1 and image2 MUST be the same
    pass

def invert_image(image):
    #creates the same image but upside down!
    pass

def create_a_border(image1,image2,start_pixels,dimension):
    #Creates a border (using image 2) around image 1
    #start pixels is either a tuple or list in the form of (x,y)
    #dimension is a list that says how wide you want the top and sides
    pass

def scramble_image(image):
    #scrambles an image into 7 parts to form a basic "sliding puzzle"
    #optional challenge!
    pass