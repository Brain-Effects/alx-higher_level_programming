#!/usr/bin/python3
"""
This module sends a request to the GitHub API and displays the 10 most recent
commits (from the most recent to oldest) of the specified repository by the
specified user.
"""

import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:
            print("{}: {}".format(commit.get('sha'), commit.get(
                'commit').get('author').get('name')))
