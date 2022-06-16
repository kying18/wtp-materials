# car.py
# Name:
# Collaborators:

# Program for drawing and moving a car

from graphics import *

win = GraphWin("Car", 300, 300)
rect = Rectangle(Point(10,10), Point(100,100))

rect.setFill("blue")
rect.draw(win)

win.getMouse()
win.close()  