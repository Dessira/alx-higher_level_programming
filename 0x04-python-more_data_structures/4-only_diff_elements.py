#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff = []
    for i in set_1:
        var = i
        if var not in set_2:
            diff += [i]
    for j in set_2:
        val = j
        if val not in set_1:
            diff += [j]
    return diff
