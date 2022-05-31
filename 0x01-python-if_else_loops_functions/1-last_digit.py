#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    i = number % 10
else:
    i = ((number * -1) % 10) * -1

if (i < 6) and not(i == 0):
    print(f"Last digit of {number:d} is {i} and is less than 6 and not 0")
elif i > 5:
    print(f"Last digit of {number:d} is {i} and is greater than 5")
else:
    print(f"Last digit of {number:d} is {i} and is 0")
