#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    val = list(a_dictionary.keys())[0]
    high = a_dictionary[val]
    for i, j in a_dictionary.items():
        if j > high:
            high = j
            k = i
    return k
