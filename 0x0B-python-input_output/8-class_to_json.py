#!/usr/bin/python3
"""Returns description for JSON serialization of an object"""


def class_to_json(obj):
    """Function that returns the dictionary description
    with simple data structure
    for JSON serialization of an object

    Args:
    obj (object): object to check
    """

    return obj.__dict__
