#!/usr/bin/python3
"""Displays the value of the X-Request-Id variable found in
the header of the response for a given URL.
"""

if __name__ == "__main__":
    import urllib.request
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script_name.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.headers.get('X-Request-Id')
            if x_request_id is not None:
                print(x_request_id)
            else:
                print("X-Request-Id not found in the response header.")
    except urllib.error.URLError as e:
        print("Error:", e.reason)
