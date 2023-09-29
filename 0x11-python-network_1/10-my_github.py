#!/usr/bin/python3
"""
Takes my Github credentials (username & password)
and uses the Github API to display my ID.
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

def get_github_id(username, password):
    auth = HTTPBasicAuth(username, password)
    response = requests.get('https://api.github.com/user', auth=auth)
    return response.json().get('id')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./github_id.py <username> <access_token>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    github_id = get_github_id(username, password)
    print(github_id)
