#!/usr/bin/python3
"""script that takes in a letter"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) == 1:
        payload = {'q': ""}
    else:
        payload = {'q': sys[1]}

    r = requests.post('http://0.0.0.0:5000/search_user', param=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
