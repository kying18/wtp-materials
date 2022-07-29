class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_rec_area(self):
        return self.width * self.height

    def get_diagonal_length(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_mini_rec(self, factor):
        new_rec = Rectangle(self.width/factor, self.height / factor)
        return new_rec

    def is_square(self):
        return False


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def is_square(self):
        return True


rec = Rectangle(100, 200)
square = Square(50)

print("Rectangle: ")
print(rec.is_square())
print("Square:")
print(square.is_square())
