#!/usr/bin/python3
def magic_calculation(a, b):
    sum = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                sum += a ** b / i
            except:
                sum = a + b
                break
            return sum
