#!/usr/bin/python3
if __name__ = "__main__":
    import hidden_4
    contents = dir(hidden_4)
    size = len(contents)
    for i in range(0, size):
        if contents[i] != '__':
            print(contents[i])
