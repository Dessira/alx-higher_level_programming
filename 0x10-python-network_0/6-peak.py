#!/usr/bin/python3
"""Module containing Peak function"""


def find_peak(list_of_integers):
    """Finds and returns the peak number
    """
    size = len(list_of_integers)

    if size == 0:
        return None
    if size == 1:
        return list_of_integers[0]
    if size == 2:
        return max(list_of_integers)
    for i in range(1, size - 1):
        if list_of_integers[i] >= list_of_integers[i - 1] and\
        list_of_integers[i] >= list_of_integers[i + 1]:
            return list_of_integers[i]
