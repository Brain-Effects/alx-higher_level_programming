#!/usr/bin/python3
"""
This module contains a function that appends a string at the end of a
text file (UTF8) and returns the number of characters added.

The function creates the file if it doesn’t exist.
The function does not handle file permission or
file doesn't exist exceptions.
No modules are imported for this function.
"""


def append_write(filename="", text=""):
    """
    Function to append a string at the end of a text file and
    return the number of characters added.

    Args:
        filename (str): The name of the file to be appended to.
        Defaults to an empty string.
        text (str): The text to be appended to the file.
        Defaults to an empty string.

    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
