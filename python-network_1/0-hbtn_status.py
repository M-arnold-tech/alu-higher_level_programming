#!/usr/bin/python3
"""Python script that fetches http://0.0.0.0:5050/status"""

import urllib.request

if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"

    with urllib.request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8")))
