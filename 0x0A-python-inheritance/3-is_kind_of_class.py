#!/usr/bin/python3
"""Contains is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """function that returns True if the object is an instance of,
    or False if not
    """

    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
