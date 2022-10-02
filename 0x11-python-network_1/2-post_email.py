#!/usr/bin/python3
"""script that takes in a URL and an email,sends a POST request
displays the body of the response
"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email' : sys.argv[2]}

    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        holder = response.read()
        print(holder.decode("utf-8"))
