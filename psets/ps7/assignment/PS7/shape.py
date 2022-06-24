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
        Shape.__init__(4)  # sets self.num_sides to 4

    def find_area(self):
        raise NotImplementedError("You should implement this")

    def find_perimeter(self):
        raise NotImplementedError("You should implement this")


class Square(Rectangle):
    """Square defined by side, the length of one side in cm"""

    def __init__(self, side):
        raise NotImplementedError("You should implement this")
        # how can you use what is already set up in the Rectangle parent class?


class Circle(Shape):
    """ Circle defined by radius in cm"""

    def __init__(self, radius):
        Shape.__init__(0)
        self.radius = radius

    def find_area(self):
        raise NotImplementedError("You should implement this")
        # hint: math.pi gives pi to 15 decimal places as a float

    def find_perimeter(self):
        raise NotImplementedError("You should implement this")


class Triangle(Shape):
    """ Triangle defined by base and height"""

    def __init__(self, base, height):
        raise NotImplementedError("You should implement this")

    def find_area(self):
        raise NotImplementedError("You should implement this")

# Test out your implementation

# TODO
