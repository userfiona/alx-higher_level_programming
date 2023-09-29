#!/usr/bin/python3
"""
Lists 10 commits from the most recent to the oldest
of the repository "rails" by the user "rails".
"""

import sys
import requests

def list_recent_commits(repo_name, owner):
    url = f'https://api.github.com/repos/{owner}/{repo_name}/commits'
    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print(f'{sha}: {author_name}')

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner = sys.argv[2]

    list_recent_commits(repo_name, owner)
