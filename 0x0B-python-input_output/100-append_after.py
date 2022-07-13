#!/usr/bin/python3
"""Inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """A function that inserts a line of text to a file
    after each line containing a specific string
    Args:
    filename (string): name of the file to be used
    search_string (string): text to search for
    new_string (string): string to be appended
    """

    with open(filename, mode='r+', encoding='utf-8') as chicken:
        holder = chicken.readlines()

    idx = 0
    with open(filename, mode='w', encoding='utf-8') as icecream:
        for line in holder:
            idx += 1
            if search_string in line:
                holder.insert(idx, new_string)
        for line in holder:
            icecream.write(line)
