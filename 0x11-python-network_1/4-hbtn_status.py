#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"

    try:
        res = requests.get(url)
        res.raise_for_status()  # Raise an exception for HTTP errors (4xx and 5xx)

        print("Body response:")
        print("\t- type: {}".format(type(res.text)))
        print("\t- content: {}".format(res.text))
        except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
