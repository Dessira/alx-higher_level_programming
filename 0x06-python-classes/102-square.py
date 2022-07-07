#!/usr/bin/python3
"""Module for creating a square"""


class Square:
    """Class Square that defines a square based on 3-square.py

    Attributes:
    __size (int): Private instance attribute
    """

    def __init__(self, size=0):
        """Initializes the attributes to be used in methods

        Args:
        self (int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """Set the size of the squre"""
        return(self.__size)

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size

    def __eq__(self, comp):

        """Comparing == based on square"""
        return self.area() == comp.area()

    def __ne__(self, comp):

        """Comparing != based on square"""
        return self.area() != comp.area()

    def __lt__(self, comp):

        """Comparing < based on square"""
        return self.area() < comp.area()

    def __le__(self, comp):

        """Comparing <= based on square"""
        return self.area() <= comp.area()

    def __gt__(self, comp):

        """Comparing > based on square"""
        return self.area() > comp.area()

    def __ge__(self, comp):

        """Comparing >= based on square"""
        return self.area() >= comp.area()
