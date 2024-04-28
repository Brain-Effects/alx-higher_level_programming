#!/usr/bin/python3
"""
This module takes GitHub credentials (username and personal access token),
sends a request to the GitHub API, and displays the user id.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    response = requests.get(
            'https://api.github.com/user', auth=(username, token))
    try:
        print(response.json().get('id'))
    except ValueError:
        print("Not a valid JSON")
