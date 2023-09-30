#!/usr/bin/python3
"""
Fetches your GitHub user ID using Basic Authentication.
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    github_api_url = "https://api.github.com/user"
    github_username = sys.argv[1]
    personal_access_token = sys.argv[2]

    response = requests.get(
        github_api_url,
        auth=HTTPBasicAuth(github_username, personal_access_token)
    )

    user_info = response.json()
    user_id = user_info.get("id")

    if user_id:
        print(f"GitHub User ID: {user_id}")
    else:
        print("Unable to retrieve user ID. Please check your credentials.")
