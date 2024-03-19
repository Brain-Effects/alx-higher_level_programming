#!/usr/bin/python3
"""
The `json` module is a part of the standard library in Python.
It provides methods to parse JSON strings and convert Python data
structures to JSON format.
"""
import json


def from_json_string(my_str):
    """
    This function takes a JSON string and converts it into a Python object.

    Parameters:
    my_str (str): A string in JSON format.

    Returns:
    object: A Python object that represents the JSON string.

    Note:
    This function does not handle exceptions if the JSON string does not
    represent a valid object.
    If you pass an invalid JSON string to this function, it will
    raise a json.JSONDecodeError.
    """
    return json.loads(my_str)
