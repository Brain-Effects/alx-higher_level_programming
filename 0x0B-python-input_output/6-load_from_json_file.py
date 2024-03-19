#!/usr/bin/python3
"""
The `json` module is a part of the standard library in Python.
It provides methods to parse JSON strings and convert
Python data structures to JSON format.
"""
import json


def load_from_json_file(filename):
    """
    This function creates an object from a JSON file.

    Parameters:
    filename (str): The name of the file to read from.

    Returns:
    object: A Python object that represents the JSON data in the file.

    Note:
    This function does not handle exceptions if the JSON string does
    not represent a valid object or if there are file permission issues.
    """
    with open(filename, 'r') as f:
        return json.load(f)
