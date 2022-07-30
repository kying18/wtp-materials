from re import S
from image import Image
import numpy as np
import random
#import PIL.Image

#pip3 show numpy, then access from there, move you
def brighten(image, factor):
    # when we brighten, we just want to make each channel higher by some amount 
    # factor is a value > 0, how much you want to brighten the image by (< 1 = darken, > 1 = brighten)
        temp_Image=Image(image.array.shape[0],image.array.shape[1],image.array.shape[2])
        for i in range(image.array.shape[0]):
            for z in range(image.array.shape[1]):
                for l in range(image.array.shape[2]):
                    temp_Image.array[i][z][l]= image.array[i][z][l]*factor
        return temp_Image



def adjust_contrast(image, factor, mid):
    # adjust the contrast by increasing the difference from the user-defined midpoint by factor amount
    temp_Image=Image(image.array.shape[0],image.array.shape[1],image.array.shape[2])
    for i in range(image.array.shape[0]):
            for z in range(image.array.shape[1]):
                for l in range(image.array.shape[2]):
                    temp_Image.array[i][z][l]= (image.array[i][z][l]-mid)*factor+mid
    return temp_Image


def scramble_image(image):
    #scrambles into 8 pieces. Depending on how close the pieces are to their original area, the amount they brighten
    #and contrast will differ. 
    temp_Image=Image(image.array.shape[0],image.array.shape[1],image.array.shape[2])
    how_many=0
    length=int(image.array.shape[0]/2)
    #across is y, down is x
    height=int(image.array.shape[1]/4)
    possible_options=[[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3]]
    counter_y=-1
    counter_x=-1
    for s in range(7):
        start=random.choice(possible_options)
        possible_options.remove(start)
        x_start= start[0]
        y_start=start[1]
        for i in range(x_start*length,x_start*length+length):
            counter_x+=1
            for z in range(y_start*height,y_start*height+height):
                    counter_y+=1
                    for m in range(image.array.shape[2]):
                        if counter_y>height*(how_many+1)-1:
                            counter_y=height*how_many
                        if counter_x>length*2-1:
                            counter_x=0
                            how_many+=1
                        pixel=image.array[i][z][m]
                        temp_Image.array[counter_x][counter_y][m]= pixel

    return temp_Image


#could do motion blur?
def motion_blur(image, kernel_size):
    # kernel size is the number of pixels to take into account when applying the blur (how wide) averageing pixels surrounding
    # (ie kernel_size = 3 would be neighbors to the left/right, top/bottom, and diagonals)
    # kernel size should always be an *odd* number
    x_pixels, y_pixels, num_channels = image.array.shape  # represents x, y pixels of image, # channels (R, G, B)
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)  # making a new array to copy values to!
    neighbor_range = kernel_size // 2  # this is a variable that tells us how many neighbors we actually look at (ie for a kernel of 3, this value should be 1)
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                # we are going to use a naive implementation of iterating through each neighbor and summing
                # there are faster implementations where you can use memoization, but this is the most straightforward for a beginner to understand
                total = 0
                for y_i in range(max(0,y-neighbor_range), min(new_im.y_pixels-1, y+neighbor_range)+1):
                        total += image.array[x, y_i, c]
                new_im.array[x, y, c] = total / (kernel_size)
    return new_im

def blur(image, kernel_size):
    # kernel size is the number of pixels to take into account when applying the blur (how wide) averageing pixels surrounding
    # (ie kernel_size = 3 would be neighbors to the left/right, top/bottom, and diagonals)
    # kernel size should always be an *odd* number
        x_pixels, y_pixels, num_channels = image.array.shape  # represents x, y pixels of image, # channels (R, G, B)
        new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)  # making a new array to copy values to!
        neighbor_range = kernel_size // 2  # this is a variable that tells us how many neighbors we actually look at (ie for a kernel of 3, this value should be 1)
        for x in range(x_pixels):
            for y in range(y_pixels):
                for c in range(num_channels):
                # we are going to use a naive implementation of iterating through each neighbor and summing
                # there are faster implementations where you can use memoization, but this is the most straightforward for a beginner to understand
                    total = 0
                    for x_2 in range(-neighbor_range,neighbor_range+1):
                        for y_2 in range(-neighbor_range,neighbor_range+1):
                            if (x_2+x>0 and x_2+x<x_pixels) and (y_2+y>0 and y_2+y<y_pixels):
                                total += image.array[x_2+x, y_2+y, c]
                            else:
                                continue
                    new_im.array[x, y, c] = total / (kernel_size**2)
        return new_im


def apply_kernel(image, kernel):
    # the kernel should be a 2D array that represents the kernel we'll use!
    # for the sake of simiplicity of this implementation, let's assume that the kernel is SQUARE
    # for example the sobel x kernel (detecting horizontal edges) is as follows:
    # [1 0 -1]
    # [2 0 -2]
    # [1 0 -1]
        x_pixels, y_pixels, num_channels = image.array.shape  # represents x, y pixels of image, # channels (R, G, B)
        temp_Image = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)  # making a new array to copy values to!
        kernel_size=kernel.shape[0]
        neighbor_range = kernel_size // 2  # this is a variable that tells us how many neighbors we actually look at (ie for a kernel of 3, this value should be 1)
        for i in range(x_pixels):
            for z in range(y_pixels):
                for l in range(num_channels):
                # we are going to use a naive implementation of iterating through each neighbor and summing
                # there are faster implementations where you can use memoization, but this is the most straightforward for a beginner to understand
                    total = 0
                    for x_2 in range(-neighbor_range,neighbor_range+1):
                        for y_2 in range(-neighbor_range,neighbor_range+1):
                             x_kernel = x_2+neighbor_range
                             y_kernel = y_2+neighbor_range
                             value=kernel[x_kernel,y_kernel]
                             if (x_2+i>=0 and x_2+i<x_pixels) and (y_2+z>=0 and y_2+z<y_pixels):
                                total+=image.array[x_2+i,y_2+z,l]*value
                             else:
                                continue
                    temp_Image.array[i,z,l]=total
        return temp_Image

#immediately if x=0 then the y doesn't matter 

def combine_images(image1, image2):
    temp_Image=Image(image1.array.shape[0],image1.array.shape[1],image1.array.shape[2])
    for i in range(image1.array.shape[0]):
            for z in range(image1.array.shape[1]):
                for l in range(image1.array.shape[2]):
                        temp_Image.array[i][z][l]= (image1.array[i][z][l]**2+image2.array[i][z][l]**2)**(0.5)
    return temp_Image
#read the image backwards

def invert_image(image):
    temp_Image=Image(image.array.shape[0],image.array.shape[1],image.array.shape[2])
    x_value=image.array.shape[0]
    y_value=-1
    for i in range(image.array.shape[0]):
        x_value-=1
        for z in range(image.array.shape[1]):
            y_value+=1
            if y_value>image.array.shape[1]-1:
                y_value=0
            for l in range(image.array.shape[2]):
                temp_Image.array[x_value][y_value][l]= image.array[i][z][l]
    return temp_Image

#challenge is create a simple border
def create_a_border(image1,image2,start_pixls,dimension):
    #image 2 is border
    #what we want to do is go through length, down, repeat how many times wide
    #if either the first few pixels or last also fill in 
    #subtract pixel height
    temp_Image=Image(image1.array.shape[0],image1.array.shape[1],image1.array.shape[2])
    x=start_pixls[0]-1
    y=start_pixls[1]-1
    for i in range(image1.array.shape[0]):
        x+=1
        for z in range(image1.array.shape[1]):
                y+=1
                if y>image1.array.shape[1]-1:
                    y=0
                for l in range(image1.array.shape[2]):
                    if i<dimension[0] or i>image1.array.shape[0]-dimension[0]:
                        temp_Image.array[i][z][l]= image2.array[x][y][l]
                    elif z<dimension[1] or z>image1.array.shape[1]-dimension[1]:
                        temp_Image.array[i][z][l]= image2.array[x][y][l]
                    else:
                        temp_Image.array[i][z][l]= image1.array[x][y][l]
    return temp_Image


   
    #now we can invert image!
    rgbimg.save("input/filled.png", "PNG")
    #invert= invert_image("filled.png")
    #image now needs to be blurred
    #blurred=blur(invert,5)
    #blurred.write_image("test")
    #now need to combine with lake image, but only the bottom!!
    """background_image=Image(background_image)
    for i in range(400,400+blurred.shape[0]):
        for y in range(blurred.shape[1]):
            for d in range(0,blurred.shape[2]):
                background_image[i][y][d]=blurred[i-400][y][d]

    """

def sepia_filter(image_file_name):
    img = PIL.Image.open(image_file_name)
    image = img.convert('RGB')
    for i in range(image.size[0]):
        for z in range(image.size[1]):
                red=int((image.getpixel((i,z))[0] * .393) + (image.getpixel((i,z))[1] *.769) + (image.getpixel((i,z))[2] * .189))
                green=int((image.getpixel((i,z))[0] * .349) + (image.getpixel((i,z))[1] *.686) + (image.getpixel((i,z))[2] * .168))
                blue= int((image.getpixel((i,z))[0] * .272) + (image.getpixel((i,z))[1] *.534) + (image.getpixel((i,z))[2] * .131))
                if red>255:
                    red=255
                if green>255:
                    green=255
                if blue>255:
                    blue=255
                image.putpixel((i,z),(red,green,blue))
    
    image.save("output/sepia_filter.png", "PNG")



if __name__ == '__main__':
   lonk1= "input/pokemon.png"
   lonk2= "input/pika.png"
 
   #hi=sepia_filter(lonk1)
  # test=reflecting_on_water(lonk2,lonk1,[[255,216,35],[0,0,0],[234,78,35],[32,21,21],[180,59,64],[101,27,25]],[88,166,189])
   # nature=Image(filename="lake.png")
   #test=motion_blur(nature,13)

   #test.write_image("blur.png")

