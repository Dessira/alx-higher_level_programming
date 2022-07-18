#!/usr/bin/python3
"""Prints string"""


def text_indentation(text):
    """print indented  string with 2 new lines
    after each of these characters: ., ? and :"""

    chicken = ['.', '?', ':']
    c = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        i = c
        if c == len(text):
            break
        if text[i] in chicken:
            print("{}\n".format(text[i]))
            c += 1
            if i + 1 != len(text):
                if text[i + 1] == " ":
                    c += 1
        else:
            print("{}".format(text[i]), end="")
            c += 1
