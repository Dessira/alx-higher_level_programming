#!/usr/bin/python3
"""Lists the last 10 commits from a given repository
"""

import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])
    r = requests.get(url)
    res = r.json()

    try:
        for i in range(10):
            print("{}: {}".format(res[i]["sha"],
                                  res[i]["commit"]["author"]["name"]))
    except IndexError:
        pass
