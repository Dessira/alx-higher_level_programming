#!/usr/bin/python3
"""Append text to a file"""


def append_write(filename="", text=""):
    """A function that appends a string at the end of a text file (UTF8)
    returns the number of characters added
    """
    with open(filename, mode='a', encoding="utf-8") as my_file:
        count = my_file.write(text)
    return count
