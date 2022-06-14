#testing for problem 1.2 on PSET 6
import unittest
import pet
import random
class TestFeeding(unittest.TestCase):
    def test_feeding(self):
        dog = pet.Dog('a', 12.7, 'b')
        person = pet.Person('c', dog, 0.6)
        original_weight = dog.weight
        person.feedDog()
        new_weight = dog.weight
        self.assertAlmostEqual(new_weight-original_weight, person.generosity)

    def test_feeding_rand1(self):
        generosity = random.random()
        init_weight = random.random()*100
        dog = pet.Dog('a', init_weight, 'b')
        person = pet.Person('c', dog, generosity)
        original_weight = dog.weight
        person.feedDog()
        new_weight = dog.weight
        self.assertAlmostEqual(new_weight - original_weight, person.generosity)

    def test_feeding_rand2(self):
        generosity = random.random()
        init_weight = random.random()*100
        dog = pet.Dog('a', init_weight, 'b')
        person = pet.Person('c', dog, generosity)
        original_weight = dog.weight
        person.feedDog()
        new_weight = dog.weight
        self.assertAlmostEqual(new_weight - original_weight, person.generosity)

    def test_feeding_rand3(self):
        generosity = random.random()
        init_weight = random.random()*100
        dog = pet.Dog('a', init_weight, 'b')
        person = pet.Person('c', dog, generosity)
        original_weight = dog.weight
        person.feedDog()
        new_weight = dog.weight
        self.assertAlmostEqual(new_weight - original_weight, person.generosity)

    def test_feeding_rand4(self):
        generosity = random.random()
        init_weight = random.random()*100
        dog = pet.Dog('a', init_weight, 'b')
        person = pet.Person('c', dog, generosity)
        original_weight = dog.weight
        person.feedDog()
        new_weight = dog.weight
        self.assertAlmostEqual(new_weight - original_weight, person.generosity)

    def test_feeding_none(self):
        init_weight = random.random()*100
        dog = pet.Dog('a', init_weight, 'b')
        person = pet.Person('c', dog, 0)
        original_weight = dog.weight
        person.feedDog()
        new_weight = dog.weight
        self.assertAlmostEqual(new_weight - original_weight, 0)


if __name__ == '__main__':
    unittest.main()