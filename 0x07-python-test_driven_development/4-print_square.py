#!/usr/bin/python3
"""Prints a square"""


def print_square(size):
    """Function that prints a square with the character #"""
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if isinstance(size, float):
        if size < 0:
            raise TypeError("size must be an integer")
        else:
            size = int(size)
    if size < 0:
        raise TypeError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
