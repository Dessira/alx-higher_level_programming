#!/usr/bin/python3
"""Class Rectangle that defines a rectangle based on 0-rectangle.py"""


class Rectangle:
    """Class Rectangle"""
    def __init__(self, width=0, height=0):
        """initializes the attributes used by module

        Args:
        width (int): Rectangle width
        height (int): Rectangle height
        """
        self.width = width
        self.height = height

        @property
        """Set the width, check input and raise errors"""
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if type(value) != int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        """Set the height, check input and raise errors"""
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) != int:
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
