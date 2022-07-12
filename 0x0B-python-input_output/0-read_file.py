#!/usr/bin/python3
"""Reads File to stdout"""


def read_file(filename=""):
    """A function that reads a text file (UTF8) and prints it to stdout"""

    with open(filename, mode='r', encoding='utf-8') as my_file:
        chicken = my_file.read()
        for content in chicken:
            print(content, end='')
