#!/usr/bin/python3
"""Writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """A function that writes an Object to a text file,
    using a JSON representation

    Args:
    my_obj (object): object to convert
    filename (file): file
    """

    with open(filename, mode='w', encoding="utf-8") as my_file:
        json.dump(my_obj, my_file)
