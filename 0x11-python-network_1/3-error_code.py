#!/usr/bin/python3
"""
This module sends a request to a given URL and displays the body of the
response (decoded in utf-8). It also handles urllib.error.HTTPError exceptions
and prints the HTTP status code.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
