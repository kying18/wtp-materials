import unittest
import not_equal as t

class TestNotEqual(unittest.TestCase):
    def test_equal(self):
        not_equal = t.not_equal(3, 3)
        self.assertFalse(not_equal)

    def test_unequal(self):
        not_equal = t.not_equal(3, 4)
        self.assertTrue(not_equal)

    def test_equal_floats(self):
        not_equal = t.not_equal(3.14, 3.14)
        self.assertFalse(not_equal)

    def test_unequal_floats(self):
        not_equal = t.not_equal(3.14, 3.16)
        self.assertTrue(not_equal)

    def test_negative_vals(self):
        not_equal = t.not_equal(-3, 3)
        self.assertTrue(not_equal)

if __name__ == '__main__':
    unittest.main()