#!/usr/bin/python3
"""Script takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in the header
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    resp = urllib.request.Request(url)
    with urllib.request.urlopen(resp) as holder:
        print(dict(holder.headers).get('X-Request-Id'))
