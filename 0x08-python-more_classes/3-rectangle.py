#!/usr/bin/python3
"""Class Rectangle that defines a rectangle based on 2-rectangle.py"""


class Rectangle:
    """Class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes attributes

        Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set the width, check input and raise errors"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Set the height, check input and raise errors"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method calculates the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Method calculates perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__height + self.__width))

    def __str__(self):
        """prints rectangle using '#'"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            for j in range(self.__width):
                string += '#'
            if i != self.__height - 1:
                string += '\n'
        return string
