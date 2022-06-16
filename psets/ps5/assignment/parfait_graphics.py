# parfait_graphics.py
# Name :
# Collaborators :

# Draws the ladyfinger parfait recipe

from graphics import *

# create the graphics window
win = GraphWin("Ladyfinger Parfait", 300, 300)

# create text centered at (100, 100)
msg1 = Text(Point(100,100), "Hello, WTP!")
msg1.draw(win)

# process ends
win.getMouse() 
win.close()


