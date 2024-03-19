#!/usr/bin/python3
"""
The `json` module is a part of the standard library in Python.
It provides methods to parse JSON strings and convert Python
data structures to JSON format.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an object to a text file, using a JSON representation.

    Parameters:
    my_obj (object): The Python object to be written to the file.
    filename (str): The name of the file to write to.

    Note:
    This function does not handle exceptions if the object can't be
    serialized or if there are file permission issues.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
