#!/usr/bin/python3
"""A class MyList that inherits from list"""


class MyList(list):
    """class MyList that inherits from list"""
    def print_sorted(self):
        """Function prints the list in ascending sort"""
        print(sorted(self))
