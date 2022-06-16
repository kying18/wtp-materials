# simple_graphics.py
# Name :
# Collaborators :

# Program for drawing a circle

import random
from graphics import *

win = GraphWin('My Circle', 100, 100)
c = Circle(Point(50, 50), 20)
c.setFill('yellow')
c.setOutline('purple')
c.draw(win)

# optional challenge a

win.getMouse()  # pause for click in window
c2 = Circle(Point(50, 50), 16)
c2.setFill('purple')
c2.setOutline('green')
c2.draw(win)

win.getMouse()  # pause for click in window
c3 = Circle(Point(50, 50), 12)
c3.setFill('green')
c3.setOutline('red')
c3.draw(win)

win.getMouse()  # pause for click in window
c4 = Circle(Point(50, 50), 8)
c4.setFill('red')
c4.setOutline('blue')
c4.draw(win)

# optional challenge b/c
colors = ["red", "orange", "yellow", "green", "blue", "purple", "white", "black"]

win.getMouse()  # pause for click in window
x, y, radius, color = random.randint(0, 100), random.randint(0, 100), random.randint(0, 25), random.choice(colors)
c2 = Circle(Point(x, y), radius)
c2.setFill(color)
c2.draw(win)

win.getMouse()  # pause for click in window
x, y, radius, color = random.randint(0, 100), random.randint(0, 100), random.randint(0, 25), random.choice(colors)
c3 = Circle(Point(x, y), radius)
c3.setFill(color)
c3.draw(win)

win.getMouse()  # pause for click in window
x, y, radius, color = random.randint(0, 100), random.randint(0, 100), random.randint(0, 25), random.choice(colors)
c4 = Circle(Point(x, y), radius)
c4.setFill(color)
c4.draw(win)

win.getMouse()
win.close()
