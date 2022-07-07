#!/usr/bin/python3
"""Function adds new attributes"""


def add_attribute(obj, name, value):
    """Adds new attribute to an object if it's possible
    Args:
    obj (all): the object
    name (str): name of attribute
    value (all): value of the attribute name
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
