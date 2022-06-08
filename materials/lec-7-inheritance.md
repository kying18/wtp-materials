# Lecture 7: Inheritance and Polymorphism

# Sources

These notes were adapted or copied verbatim from from [Adam Hartz](https://hz.mit.edu/)'s MIT [6.145 readings](https://hz.mit.edu/catsoop/6.145/), as well as [Think Python 2e](https://greenteapress.com/wp/think-python-2e/) by [Allen Downey](http://www.allendowney.com/wp/).

# Classes (Review)

Last class, we introduced **classes** (no pun intended). Let's go through classes again using an example. Suppose we are in charge of writing some software for an animal shelter, to help them keep track of adoptions. Naturally, we would probably want to create a class for animals. Let's do that.

What is important for a shelter to note about an animal? Probably what kind of animal it is, its birthday or age, its gender, its name, just to name a few (no pun intended...).

```
class Animal:
    def __init__(self, animal_type, age, gender, name):
        self.animal_type = animal_type
        self.age = age
        self.gender = gender
        self.name = name

    # function to return the information about the animal!
    def get_bio(self):
        pronoun = "she" if self.gender == "female" else "he"
        return f'{self.name} is a {self.gender} {self.animal_type} and {pronoun} is {self.age} years old!'
```

Let's create some animals:

```
dog1 = Animal("dog", 2, "female", "Snowball")
dog2 = Animal("dog", 3, "male", "Zeus")
cat = Animal("cat", 5, "female", "Coco")
hamster = Animal("hamster", 2, "male", "Hamilton")

print(dog1.get_bio())
print(dog2.get_bio())
print(cat.get_bio())
print(hamster.get_bio())
```

Sweet.

Ok, but now, let's say we want to keep track of whether the dog is potty-trained, but that doesn't make sense for a hamster to have that attribute! That's when inheritance can come into play.

# Inheritance

In our example, we want the animals to have some similar attributes and methods, but the bigger animals differ from the smaller animals in some way. We could either copy the entire class and make two separate animals, but then there could be a lot of copy-pasting going on!

Instead, Python lets us use something called **inheritance** to accomplish this. Basically, we can create **subclasses** of the `Animal` class, so that they _inherit_ all the traits/methods of the parent class (or **superclass**)!

```
class Dog(Animal):
    def __init__(self, age, gender, name, potty_training):
        super().__init__("dog", age, gender, name)  # initializes the traits of the superclass!
        self.potty_training = potty_training
```

Now, if we re-define `dog1` and `dog2` using this new class, we get:

```
dog1 = Dog(2, "female", "Snowball", False)
dog2 = Dog(3, "male", "Zeus", True)

print(dog1.potty_training)
print(hamster.potty_training)
```

# Another Example

Still confused? Let's use another example. Let's return to our rectangles from the previous lesson:

```
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # gets area of rec
    def get_rec_area(self):
        return self.width * self.height

    # length of the diagonal from opposing corners of rectangle
    def get_diagonal_length(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5  # hypotenuse

    # returns an instance of Rectangle with 1/2 the width and 1/2 the height of the original
    def get_mini_rec(self):
        new_rec = Rectangle(self.width/2, self.height/2)
        new_rec.width = self.width / 2
        new_rec.height = self.height / 2
        return new_rec
```

Squares are a special type of rectangle where the width and height are the same! We could declare this as a subclass of `Rectangle`:

```
class Square(Rectangle):
    def __init__(self, side_len):
        super().__init__(side_len, side_len)
```

Ta da! That's it. By writing it this way, we are less likely to make an error when we actually run into squares (we could easily make a typo where the width and height are different). However, we have the flexibility to continue defining `Rectangle`s in addition to defining `Square`s! In addition, the `Square` has access to all the parent functions!

```
square = Square(4)
print(square.get_rec_area())
print(square.get_diagonal_length())
```

Sweet!

<!-- # Good Python Coding Practices

Now you know the basics of computer programming in Python. You have the foundational tools to build scripts from the ground up! Just like learning a new language, concepts will make more sense as you practice more. However, let's briefly touch on good coding practices so we can -->
