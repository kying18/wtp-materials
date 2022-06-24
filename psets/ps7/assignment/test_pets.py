import unittest

from pets import *


# NOTE TO STUDENTS: this is for the optional question
class TestPets(unittest.TestCase):
    def test_cat_speak(self):
        cat1 = Cat("cat")
        self.assertEqual((cat1.speak()).lower(), "meow", "Cat should say meow when speaking!")

    def test_dog_speak(self):
        dog1 = Dog("dog1", False)
        self.assertEqual(dog1.speak(), "bark", "Make sure your quiet dog is able to say 'bark'!")

    def test_dog_speak_loud(self):
        dog2 = Dog("dog2", True)
        self.assertEqual(dog2.speak(), "BARK", "Make sure the loud dog is able to say 'BARK'")


if __name__ == "__main__":
    unittest.main()
