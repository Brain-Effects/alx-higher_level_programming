#!/usr/bin/python3
"""
This module contains a function that writes a string to a text file
(UTF8) and returns the number of characters written.

The function does not handle file permission exceptions.
The function creates the file if it doesn’t exist.
The function overwrites the content of the file if it already exists.
No modules are imported for this function.
"""


def write_file(filename="", text=""):
    """
    Function to write a string to a text file and return the number of
    characters written.

    Args:
        filename (str): The name of the file to be written to.
        Defaults to an empty string.
        text (str): The text to be written to the file. Defaults
        to an empty string.

    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
