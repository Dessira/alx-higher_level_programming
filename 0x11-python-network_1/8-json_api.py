#!/usr/bin/python3
"""script that takes in a letter
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import sys
import requests

if __name__ = "__main__":
    if len(sys.srgv) == 1:
        payload = {'q': ""}
    else:
        payload = {'q': sys[2]}

    r = requests.post('http://0.0.0.0:5000/search_user', param=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response,get("id"), response.get("name")))
