#!/usr/bin/python3
"""Contains a function that returns True if the object is exactly an instance
else False
"""


def is_same_class(obj, a_class):
    """Function that checks the object"""

    if type(obj) == a_class:
        return True
    else:
        return False
