#!/usr/bin/python3
"""Creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """Function that creates an Object from a JSON file"""

    with open(filename, mode="r", encoding="UTF-8") as rfile:
        return json.load(rfile)
