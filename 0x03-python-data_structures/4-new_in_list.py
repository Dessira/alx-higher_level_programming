#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_copy = []
    val = []
    if idx < 0 or idx > len(my_list):
        new_copy = my_list
        return new_copy
    for i in range(len(my_list)):
        if i == idx:
            new_copy = new_copy + [element]
        else:
            val = my_list[i]
            new_copy = new_copy + [val]
    return new_copy
