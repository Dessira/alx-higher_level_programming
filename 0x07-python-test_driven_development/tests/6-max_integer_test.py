#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max integer"""

    def test_empty_list(self):
        """Checks with empty list"""
        self.assertEqual(max_integer([]), None)

    def test_normal_list(self):
        """Checks with unordered list"""
        self.assertEqual(max_integer([1, 5, 3, 7, 4]), 7)

    def test_negative_list(self):
        """Checks using negative list"""
        self.assertEqual(max_integer([-1, -4, -2]), -1)

    def test_one_input_list(self):
        """Checks using list with string and int"""
        self.assertEqual(max_integer([3]), 3)

if __name__ == '__main__':
    unittest.main()
