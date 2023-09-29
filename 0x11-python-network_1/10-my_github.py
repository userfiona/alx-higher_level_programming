#!/usr/bin/python3
"""
Takes my GitHub credentials (username & personal access token)
and uses the GitHub API to display my ID.
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

def get_github_id(username, token):
    auth = HTTPBasicAuth(username, token)
    response = requests.get('https://api.github.com/user', auth=auth)

    if response.status_code == 200:
        return response.json().get('id')
    else:
        print(f"Error: {response.status_code}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./github_id.py <username> <personal_access_token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    github_id = get_github_id(username, token)
    print(github_id)
