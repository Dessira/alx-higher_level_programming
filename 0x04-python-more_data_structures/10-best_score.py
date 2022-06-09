#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    val = list(a_dictionary.keys())[0]
    high = a_dictionary[val]
    for i in a_dictionary:
        if a_dictionary[i] > high:
            high = a_dictionary[i]
            k = i
    return k
