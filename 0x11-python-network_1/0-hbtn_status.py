#!/usr/bin/python3
"""
    This module fetches and displays the status of a webpage.

    The script uses the urllib package to send a request to a given URL
    and then prints out the type, content, and utf8 content of the response.
"""


import urllib.request


def fetch_status():
    """
    Fetch and print the status of a webpage.

    The function opens the URL using urlopen from urllib.request,
    reads the response using the read method, and then prints the
    type, content, and utf8 content of the response.
    """


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf-8')))


if __name__ == "__main__":
    fetch_status()
