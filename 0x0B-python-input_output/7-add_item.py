#!/usr/bin/python3
"""
This module provides functions to add command line arguments to
a list and save them to a file in JSON format.

Functions:
- save_to_json_file(my_obj, filename): Writes a Python object to
a file in JSON format.
- load_from_json_file(filename): Reads JSON data from a file and
returns a Python object.

Note:
These functions do not handle exceptions if the object can't be serialized
or if there are file permission issues.
"""

import sys
import json
import os


def save_to_json_file(my_obj, filename):
    """
    This function writes an object to a text file, using a JSON representation.

    Parameters:
    my_obj (object): The Python object to be written to the file.
    filename (str): The name of the file to write to.

    Note:
    This function does not handle exceptions if the object can't
    be serialized or if there are file permission issues.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)


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

filename = "add_item.json"
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []


my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename
