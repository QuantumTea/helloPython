import unittest
from maths import *


class TestMaths(unittest.TestCase):
    def test_list_int(self):
        # Test that it can sum a list of integers
        data = [1, 2, 3, 4, 5]
        result = my_sum(data)
        self.assertEqual(15, result)

    def test_multiply_2_numbers(self):
        result = my_multiply(2, 4)
        self.assertEqual(8, result)

    def test_square(self):
        result = my_square(3)
        self.assertEqual(9, result)

    def test_cube(self):
        result = my_cube(3)
        self.assertEqual(27, result)

    def test_factorial(self):
        # Use the built-in function
        result = factorial(5)
        self.assertEqual(120, result)

    def test_factorial_with_recursion(self):
        # Write your own recursion
        result = factorial_with_recursion(6)
        self.assertEqual(720, result)
