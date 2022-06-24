# simple_graphics.py
# Name :
# Collaborators :

# Program for drawing a circle

from graphics import *

win = GraphWin('My Circle', 100, 100)
c = Circle(Point(50, 50), 10)
c.setFill('red')
c.draw(win)

win.getMouse() # pause for click in window
win.close()

