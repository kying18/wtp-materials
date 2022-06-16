# pet.py
# Name:
# Collaborators:
#
class Dog():
    def __init__(self, name, weight, breed):
        self.name=name
        self.weight=weight
        self.breed=breed
        
    def eat(self, amount):
        self.weight+=amount

    def exercise(self, amount):
        self.weight-=amount
        
class Person():
    def __init__(self, name, dog, generosity):
        self.name=name
        self.dog=dog
        self.generosity=generosity
        
    def feedDog(self):
        ## YOUR CODE HERE
        pass



## YOUR CODE HERE
## Create a Dog object. (Choose any name (string), weight (float), and breed (string) that you want.)

## Create a Person object.
##  -Choose any name (string) that you want.
##  -The dog parameter should be the Dog you just created. 
##  -The generosity should be any floating point number such that 0<=generosity<=1

## Have your Person object feed their pet dog.

