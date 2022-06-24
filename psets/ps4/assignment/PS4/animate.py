# animate.py
# Name:
# Collaborators:

from graphics import *
from time import sleep   # for pausing between frames

win = GraphWin("Ball", 300, 300)

# a circle is drawn at position (100, 150) on the board
c = Circle(Point(100, 150), 25)
c.setFill('red')
c.draw(win)

# wait 1 second
time.sleep(1)
# move the circle 50 pixels in the x direction and 0 pixels in y
c.move(50, 0)

win.getMouse() 
win.close()