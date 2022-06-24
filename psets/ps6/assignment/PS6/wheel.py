# wheel.py
# Name:
# Collaborators:

# Program for drawing a moving wheel

from graphics import *

class Wheel(object):
    def __init__(self, center, wheel_radius, tire_radius):
        #Our wheel is constructed with a center point, and a radius for the wheel and the tire.
        
        self.tire_circle = Circle(center, tire_radius)
        
        #The tire circle attribute is another object: a circle.
        self.wheel_circle = Circle(center, wheel_radius)
        
    def draw(self, win):
        #We want to be able to draw our Wheel, so we have to make a method for that.
        self.tire_circle.draw(win)
        
        #Here, we are using the draw method built into Python. self.tire_circle 
        #is a Circle object, so we are calling the draw method on that object.
        self.wheel_circle.draw(win)
        
    def move(self, dx, dy):
        #We also want to be able to move the wheel (it is a wheel after all!)
        self.tire_circle.move(dx, dy)
        
        #Python has a built-in move method too. We are calling it on the self.tire_circle 
        #Circle object here. move takes two parameters – the change in x and
        #the change in y that it should move.
        self.wheel_circle.move(dx, dy)
        
    def set_color(self, wheel_color, tire_color):
        #We also want to be able to set its color. We have to remake all of these
        #methods because we are making a new class, but it is okay to just tell it to
        #do these things on objects we already have.
        self.tire_circle.setFill(tire_color)
        self.wheel_circle.setFill(wheel_color)
        
    def undraw(self): 
        #This method will undraw itself--get rid of the image.
        self.tire_circle.undraw()
        self.wheel_circle.undraw()

    def get_size(self):
        return self.tire_circle.getRadius()
    #Circle has a built-in method that gets the radius--here we arejust calling
    #it on the tire_circle object, which is an instance of Circle.
    
    def get_center(self):
        return self.tire_circle.getCenter() #getcenter is built into Circle too.

win = GraphWin('Wheel', 320, 240)
w = Wheel(Point(100, 100), 50, 70)#This creates a new object w that is a Wheel.
w.draw(win)
w.set_color('gray', 'black')

win.getMouse()
win.close()  
