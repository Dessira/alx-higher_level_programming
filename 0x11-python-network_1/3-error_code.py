#!/usr/bin/python3
"""cript that takes in a URL, sends a request to the URL and displays the body of the response
"""

import sys
import urllib.parse
import urllib.request

if __name__ = "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as f:
            print(f.read(),decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: ", e.code)