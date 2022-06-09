#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = a_dictionary.copy()
    for i, j in new.items():
        if value in j:
            del a_dictionary[i]
    return a_dictionary
