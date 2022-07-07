#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """Class based on 6-base_geometry"""

    def area(self):
        """Method that defines the area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates values Recieved"""

        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
