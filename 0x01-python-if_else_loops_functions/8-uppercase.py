#!/usr/bin/python3
def uppercase(str):
    str2 = ""
    for i in range(len(str)):
        if ord(str[i]) >96 and ord(str[i]) < 123:
            str2[i] += chr(ord(str[i]) - 32)
        str2[i] += str[i]
    print("{:c}".format(str2))
