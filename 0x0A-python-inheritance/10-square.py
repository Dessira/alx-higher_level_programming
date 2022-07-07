#!/usr/bin/python3
"""Class Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that inherits from Rectangle"""

    def __init__(self, size):
        """instanstion of attributes
        Args:
            size (int): size of square
        """

        super().integer_validator("size", size)
        super().__init__(size, size)

        self.__size = size

    def area(self):
        """Returns area of square"""

        return self.__size * self.__size
