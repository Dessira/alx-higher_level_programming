#!/usr/bin/python3
"""Returns a list object"""


def lookup(obj):
    """A function that returns the list of available
    attributes and methods of an object
    """
    return [dir(obj)]
