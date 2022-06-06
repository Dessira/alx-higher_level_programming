#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0 or my_list is None:
        return None
    high = 0
    for index in my_list:
        if index > high:
            high = index
    return high
