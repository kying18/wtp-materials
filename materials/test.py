class Car:
    weight = 1000

    def __init__(self, weight, driver):
        self.weight = weight
        self.driver = driver


class Person:
    weight = 100

    def __init__(self, weight):
        self.weight = weight


print(Car.driver.weight)
