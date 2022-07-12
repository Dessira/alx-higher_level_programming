#!/usr/bin/python3
"""Writes a new  text to a file"""


def write_file(filename="", text=""):
    """A function that writes a string to a text file (UTF8)
    returns the number of characters written
    """
    with open(filename, mode='w', encoding="utf-8") as my_file:
        count = my_file.write(text)
    return count
