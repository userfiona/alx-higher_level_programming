#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status and displays its content
and the value of the X-Request-Id header using urllib.
"""

if __name__ == "__main__":
    import urllib.request
    import sys

    url = "https://alx-intranet.hbtn.io/status"

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')

        x_request_id = response.headers.get('X-Request-Id')

        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data))
        print("\t- X-Request-Id: {}".format(x_request_id))

    except urllib.error.URLError as e:
        print("Error:", e.reason)
