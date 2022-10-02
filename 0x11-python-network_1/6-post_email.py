#!/usr/bin/python3
""" script that takes in a URL and an email address, sends a POST request
displays the body of the response
"""

import sys
import requests

if __name__ == "__main__":

    value = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], params=value)
    print(r.text)
