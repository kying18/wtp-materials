
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
        return "Meow" 


class Dog(Pet):
    """
        name: the dog's name
        loud: a boolean, if True the dog is loud and if False it is not
    """
    def __init__(self,name,loud):
        self.name=name
        self.loud=loud

    def speak(self):
        if self.loud:
            return (self.speak_with_volume())
        else:
            return "bark"
    
    """
        returns "BARK" in all caps if the dog is loud and "bark" otherwise
    """
    def speak_with_volume(self):
       return "BARK"



# Test out the following function to make sure it works correctly for your implementation of the Cat and Dog objects

def print_pet_sounds(pet,times):
        for i in range(times):
            print(pet.speak())
    

def print_dog_sounds(dog,times):
        for i in range(times):
            print(dog.speak_with_volume())

cat1=Cat("cat :)")
print_pet_sounds(cat1,3)
dog1=Dog("dog1 :)",False)
print_pet_sounds(dog1,3)

dog2=Dog("dog2 :)",True)
print_pet_sounds(dog2,3)

dog3=Dog("dog3 :)", True)
print_dog_sounds(dog3,3)


# Questions:
# Is it okay that Dog has a function that Cat and Pet don't have?
#Yes! Dog is a child class unrelated to Cat.

# What does the fact that speak throws an error for the Pet object 
# tell us about the intended use for the Pet object?

#Pet is just placement holder! It is meant to be refined in the children class

# Would it be okay to make another Pet object that didn't implement
# the speak function? What would happen to the print_pet_sounds function?
# Would it still work?

#Yes. print_pet_sounds would give the NotImplementedError, as it would give the parent class' function. 


