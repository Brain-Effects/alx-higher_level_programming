#!/usr/bin/python3
"""
This module sends a POST request to a given URL with an email as a parameter,
and displays the body of the response (decoded in utf-8).
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)
