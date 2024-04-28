#!/usr/bin/python3
"""
This module sends a request to a given URL and displays the body of the
response. If the HTTP status code is greater than or equal to 400, it prints
"Error code: " followed by the value of the HTTP status code.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
