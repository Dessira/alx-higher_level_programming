#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    skip = len(my_list)
    for i in range(skip - 1, -1, -1):
        print("{:d}".format(my_list[i]))
