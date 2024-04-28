#!/usr/bin/python3
"""
This module fetches and displays the status of a webpage.

The script uses the requests package to send a request to a given URL
and then prints out the type and content of the response.
"""

import requests

if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
