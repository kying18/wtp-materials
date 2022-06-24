#testing for problem 1.2 on PSET 6
import unittest
import pet

class TestFeeding(unittest.TestCase):
    def test_feeding(self):
        dog = pet.Dog('a', 12.7, 'b')
        person = pet.Person('c', dog, 0.6)
        original_weight = dog.weight
        person.feedDog()
        new_weight = dog.weight
        self.assertAlmostEqual(new_weight-original_weight, person.generosity)

    def test_feeding_2(self):
        dog = pet.Dog('a', 147.45, 'b')
        person = pet.Person('c', dog, 0.8)
        original_weight = dog.weight
        person.feedDog()
        new_weight = dog.weight
        self.assertAlmostEqual(new_weight-original_weight, person.generosity)

    def test_feeding_light_dog(self):
        dog = pet.Dog('a', 0, 'b')
        person = pet.Person('c', dog, 0.5)
        original_weight = dog.weight
        person.feedDog()
        new_weight = dog.weight
        self.assertAlmostEqual(new_weight-original_weight, person.generosity)

    def test_feeding_max(self):
        dog = pet.Dog('a', 7, 'b')
        person = pet.Person('c', dog, 1)
        original_weight = dog.weight
        person.feedDog()
        new_weight = dog.weight
        self.assertAlmostEqual(new_weight-original_weight, person.generosity)

    def test_feeding_twice(self):
        dog = pet.Dog('a', 14.7, 'b')
        person = pet.Person('c', dog, 0.5)
        original_weight = dog.weight
        person.feedDog()
        person.feedDog()
        new_weight = dog.weight
        self.assertAlmostEqual(new_weight-original_weight, 2*person.generosity)

    def test_feeding_thrice(self):
        dog = pet.Dog('a', 14.7, 'b')
        person = pet.Person('c', dog, 0.5)
        original_weight = dog.weight
        person.feedDog()
        person.feedDog()
        person.feedDog()
        new_weight = dog.weight
        self.assertAlmostEqual(new_weight-original_weight, 3*person.generosity)


    def test_feeding_none(self):
        init_weight = 17.8
        dog = pet.Dog('a', init_weight, 'b')
        person = pet.Person('c', dog, 0)
        original_weight = dog.weight
        person.feedDog()
        new_weight = dog.weight
        self.assertAlmostEqual(new_weight - original_weight, 0)


if __name__ == '__main__':
    unittest.main()