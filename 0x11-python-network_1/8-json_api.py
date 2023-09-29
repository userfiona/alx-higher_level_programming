#!/usr/bin/python3
"""
Given a letter as a parameter, POST to http://0.0.0.0:5000/search_user
Usage: ./8-json_api.py [letter only]
"""
import sys
import requests

def search_user(letter=""):
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': letter}
    response = requests.post(url, data=payload)

    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

        if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

        search_user(letter)
