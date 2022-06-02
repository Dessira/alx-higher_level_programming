#!/usr/bin/python3
if __name__ = "__main__":
    from hidden_4 import *
    contents = dir(hidden_4)
    size = len(contents)
    for i in range(size):
        if contents[i] != '__':
            print(contents[i])
