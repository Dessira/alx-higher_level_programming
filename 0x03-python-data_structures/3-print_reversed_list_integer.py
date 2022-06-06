#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    skip = len(my_list)
    for i in range(skip - 1, -1, -1):
        print("{:d}".format(my_list[i]))
    print()
