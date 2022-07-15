#!/usr/bin/python3
"""Unittest for Base class
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests the Base class
    """

    def test_base_id(self):
        """Tests basic use of base.id"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_input_id(self):
        """Test for input id"""
        b2 = Base(12)
        self.assertEqual(b2.id, 12)

    def test_current_id(self):
        """Check if id assigned increaments by 1"""
        b3 = Base()
        self.assertEqual(b3.id, 2)

if __name__ == "__main__":
    unittest.main()
