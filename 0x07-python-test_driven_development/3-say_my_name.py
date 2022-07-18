#!/usr/bin/python3
"""Module prints the first name"""


def say_my_name(first_name, last_name=""):
    """Recieves input string, checks
    for errors and prints first and last name"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
