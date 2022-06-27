#!/usr/bin/python3
"""Module for creating a square"""


class Square:
    """Class Square that defines a square based on 1-square.py
    Attributes:
        __size(int): Private instance attribute"""

    def __init__(self, size=0):
        """Initializes attributes to be used by methods
        Args:
        size (int): size of square
        Raises error when:
            size is not type int
            size is less than zero

        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
