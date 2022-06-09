#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = list(set(my_list))
    sum = new_list[0]
    for i in range(1, len(new_list)):
        sum += new_list[i]
        print(sum)
    return sum
