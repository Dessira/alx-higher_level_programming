#!/usr/bin/python3
"""Contains def inherits_from function"""


def inherits_from(obj, a_class):
    """Function that returns True if the object is an instance of a class
    that inherited from the specified class otherwise False
    """

    if isinstance(obj, a_class) is True and type(obj) != a_class:
        return True
    else:
        return False
