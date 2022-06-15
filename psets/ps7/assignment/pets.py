
class Pet:
    """
        name: a string, the pet's name
    """
    def __init__(self,name):
        self.name = name 

    """
        returns a lowercase string with the sound the pet makes
    """
    def speak(self):
        # this function should be implemented by the subclasses 
        raise NotImplementedError("You do not need to implement this one")

    


class Cat(Pet):
    """
        name: the cat's name
        inherits __init__ from pet (omitted here)
    """
    
    def speak(self):
        raise NotImplementedError("You should implement this")


class Dog(Pet):
    """
        name: the dog's name
        loud: a boolean, if True the dog is loud and if False it is not
    """
    def __init__(self,name,loud):
        raise NotImplementedError("You should implement this")

    def speak(self):
        raise NotImplementedError("You should implement this")
    
    """
        returns "BARK" in all caps if the dog is loud and "bark" otherwise
    """
    def speak_with_volume(self):
        raise NotImplementedError("You should implement this")



# Test out the following function to make sure it works correctly for your implementation of the Cat and Dog objects
"""
    pet: a Pet object 
    times: an int
    prints the sound made by the pet times number of times, each on a separate line
"""
def print_pet_sounds(pet,times):
    for i in range(times):
        print(pet.speak())
    
"""
    dog: a Dog object
    times: an int
     prints the sound made by the dog with volume (caps or no caps) times number of times, each on a separate line
"""
def print_dog_sounds(dog,times):
    for i in range(times):
        print(dog.speak_with_volume())


# Questions:
# Is it okay that Dog has a function that Cat and Pet don't have?

# What does the fact that speak throws an error for the Pet object 
# tell us about the intended use for the Pet object?

# Would it be okay to make another Pet object that didn't implement
# the speak function? What would happen to the print_pet_sounds function?
# Would it still work?







