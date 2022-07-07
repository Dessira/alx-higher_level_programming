#!/usr/bin/python3
"""Class Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """instantation of attributes"""

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return area of rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """Prints rectangle description"""

        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
