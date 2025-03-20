#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""

import urllib.request

if __name__ == "__main__":
    urls = ["https://intranet.hbtn.io/status", "http://0.0.0.0:5050/status"]

    for url in urls:
        try:
            with urllib.request.urlopen(url) as response:
                html = response.read()
                print("Body response:")
                print("\t- type: {}".format(type(html)))
                print("\t- content: {}".format(html))
                print("\t- utf8 content: {}".format(html.decode("utf-8")))
            break  # Stop once the correct URL works
        except Exception as e:
            pass  # Try the next URL if one fails
