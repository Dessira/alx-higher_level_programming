#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    truth_hat = []
    for index in my_list:
        if index % 2 == 0:
            truth_hat = truth_hat + [True]
        else:
            truth_hat = truth_hat + [False]
    return truth_hat
