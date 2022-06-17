# tests for PSET #6 Problem 1

import unittest
import create as create
import io
import sys


class TestClass(unittest.TestCase):
    def test_reg_list(self):
        l = [0, 1, 2]
        test = create.NewClass(l)
        self.assertEqual(test.the_list, l, "The list should be accessible through any_object.the_list")

    def test_one_list(self):
        l = [1]
        test = create.NewClass(l)
        self.assertEqual(test.the_list, l, 'ensure the null input works too!')

    def test_unsorted_list(self):
        test = create.NewClass([3, 7, 2])
        self.assertEqual([3, 7, 2], test.the_list, 'is your list autosorting?')


class TestPrintParams(unittest.TestCase):
    def test_regular(self):
        test = create.NewClass([3, 7, 2])
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        test.print_params()
        self.assertEqual(capturedOutput.getvalue(), '3\n7\n2\n')

    def test_long(self):
        test = create.NewClass([3, 7, 2, 9, 10, 1, 2, 3, 4])
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        test.print_params()
        self.assertEqual(capturedOutput.getvalue(), '3\n7\n2\n9\n10\n1\n2\n3\n4\n')


class TestAverages(unittest.TestCase):
    def test_normal(self):
        x = [12, 5, 7, 0, 9]
        average = sum(x)/len(x)
        objects = create.NewClass(x)
        test_avg = objects.find_average()
        self.assertEqual(average, test_avg, 'your average test needs to be checked')

    def test_one(self):
        x = [1]
        avg = sum(x)/len(x)
        objects = create.NewClass(x)
        test_avg = objects.find_average()
        self.assertEqual(avg, test_avg, 'how do you handle a single input?')


class TestMin(unittest.TestCase):
    def test_normal(self):
        x = [12, 5, 7, 0, 9]
        mini = min(x)
        objects = create.NewClass(x)
        test_min = objects.find_min()
        self.assertEqual(mini, test_min, 'your min test needs to be checked')

    def test_one(self):
        x = [1]
        mini = min(x)
        objects = create.NewClass(x)
        test_min = objects.find_min()
        self.assertEqual(mini, test_min, 'how do you handle a single input?')

    def test_negs(self):
        x = [1, -1, 9, 3, 2]
        mini = min(x)
        objects = create.NewClass(x)
        test_min = objects.find_min()
        self.assertEqual(mini, test_min, 'how do you handle a single input?')


class TestMax(unittest.TestCase):
    def test_normal(self):
        x = [12, 5, 7, 0, 9]
        maxi = max(x)
        objects = create.NewClass(x)
        test_max = objects.find_max()
        self.assertEqual(maxi, test_max, 'your max test needs to be checked')

    def test_one(self):
        x = [1]
        maxi = max(x)
        objects = create.NewClass(x)
        test_max = objects.find_max()
        self.assertEqual(maxi, test_max, 'how do you handle a single input?')

    def test_negs(self):
        x = [1, 3, -1, 2, -19, 20]
        maxi = max(x)
        objects = create.NewClass(x)
        test_max = objects.find_max()
        self.assertEqual(maxi, test_max, 'how do you handle a single input?')


if __name__ == '__main__':
    unittest.main()
