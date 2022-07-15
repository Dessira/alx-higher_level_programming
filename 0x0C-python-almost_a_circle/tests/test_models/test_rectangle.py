#!/usr/bin/python3
"""Unittest for class Rectangle
"""
import unittest
from io import StringIO
import os
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests the rectangle methods"""

    def test_id(self):
        """tests for object id"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

    def test_id2(self):
        """Check with increament by 1"""
        r0 = Rectangle(1, 6)
        r2 = Rectangle(7, 4)
        self.assertEqual(r2.id, r0.id + 1)
    def test_all(self):
        """checks all attributes values"""
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.id, 12)

    def test_attr_validation(self):
        """Checks attributes using positive numbers"""
        r1 = Rectangle(10, 2, 3, 4, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)


    def test_wrng_input(self):
        """checks none integer input"""
        with self.assertRaises(TypeError):
            r4 = Rectangle(9.5, 8.2, 4.4, 3,8)
            r2 = Rectangle('h', 'rome', 'goof', '#')
            r5 = Rectangle()

    def test_use_zero(self):
        """Check value error for 0 and below 0"""
        with self.assertRaises(ValueError):
            r6 = Rectangle(0, 0, -1, -1)

    def test_area(self):
        """Checks the area return value"""
        r = Rectangle(3, 2)
        r2 = Rectangle(30, 100)
        self.assertEqual(6, r.area())
        self.assertEqual(3000, r2.area())

    def test_display(self):
        """checks display output"""
        tes = Rectangle(4, 3)
        with patch('sys.stdout', new=StringIO()) as mockoutput:
            tes.display()
            self.assertEqual(mockoutput.getvalue(), '####\n####\n####\n')

        tes2 = Rectangle(2, 4, 2, 1, 3)
        with patch('sys.stdout', new=StringIO()) as mockoutput:
            tes2.display()
            self.assertEqual(mockoutput.getvalue(), '##\n##\n##\n##\n')

    def test_str(self):
        """Checks the new output printed by str"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), '[Rectangle] (12) 2/1 - 4/6')


if __name__ == '__main__':
    unittest.main()
