#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    sum = 0
    div = 0
    for index in my_list:
        sum += (index[0] * index[1])
        div += index[1]
    return (sum / div)
