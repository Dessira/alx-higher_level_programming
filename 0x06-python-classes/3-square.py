#!/usr/bin/python3
"""Module for creating a square"""


class Square:
    """Class Square that defines a square based on 2-square.py
    Attributes:
    __size (int): Private instance attribute
    """

    def __init__(self, size=0):
        """Initializes attributes used in methods
        Args:
        size (int): size of square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of a square"""
        return self.__size * self.__size
