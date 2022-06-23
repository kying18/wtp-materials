import math


class Shape():
    """ Basic shape class defined by num_sides, the number of sides of the shape """

    def __init__(self, num_sides):
        self.num_sides = num_sides

    """Returns the area of the shape in cm^2 as a float ROUNDED TO TWO DECIMALS"""

    def find_area(self):
        # this function should be implemented by the subclasses
        raise NotImplementedError("You do not need to implement this one")

    """Returns the perimeter of the shape in cm as a float ROUNDED TO TWO DECIMALS"""

    def find_perimeter(self):
        # this function should be implemented by the subclasses
        raise NotImplementedError("You do not need to implement this one")


class Rectangle(Shape):
    """ Rectangle defined by length and width in cm"""

    def __init__(self, length, width):
        Shape.__init__(self,4)  # sets self.num_sides to 4

        self.length=length
        self.width=width

    def find_area(self):
        return self.length*self.width

    def find_perimeter(self):
        return self.length*2+self.width*2


class Square(Rectangle):
    """Square defined by side, the length of one side in cm"""

    def __init__(self, side):
        # how can you use what is already set up in the Rectangle parent class?
        super().__init__(side, side)

class Circle(Shape):
    """ Circle defined by radius in cm"""

    def __init__(self, radius):
        Shape.__init__(self,0)
        self.radius = radius

    def find_area(self):
        #area=pi*r^2
        return math.pi*math.pow(self.radius,2)
        # hint: math.pi gives pi to 15 decimal places as a float

    def find_perimeter(self):
        #circumference= d*pi
        return math.pi*self.radius*2


class Triangle(Shape):
    """ Triangle defined by base and height"""

    def __init__(self, base, height):
        Shape.__init__(self, 3)
        self.base=base
        self.height=height

    def find_area(self):
        #base*height/2
        return self.base*self.height/2

