#!/usr/bin/python3

"""Max integer - Unittest"""

import unittest
from your_module_name import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_positive_numbers(self):
        result = max_integer([1, 5, 3, 2, 4])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        result = max_integer([-1, -5, -3, -2, -4])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        result = max_integer([-1, 5, 0, -2, 4])
        self.assertEqual(result, 5)

    def test_duplicate_numbers(self):
        result = max_integer([1, 2, 3, 3, 2, 1])
        self.assertEqual(result, 3)

    def test_single_element(self):
        result = max_integer([5])
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
