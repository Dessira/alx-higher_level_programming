#!/usr/bin/python3
"""Base Class"""


class Base:
    """base class for subsequnt classes

    Args:
    __nb_objects (int) = number of objects created
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the attributes to be used

        Args:
        id (int): id of the object
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
