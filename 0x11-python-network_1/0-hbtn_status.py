#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as f:
        holder = f.read()

        print("Body response:")
        print("\t- type: {}".format(type(holder)))
        print("\t- content: {}".format(holder))
        print("\t- utf8 content: {}".format(holder.decode('utf-8')))
