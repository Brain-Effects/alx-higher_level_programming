#!/usr/bin/python3
"""
This module contains a function that returns the JSON representation
of an object (string).

The function does not handle exceptions if the object can't be serialized.
No modules are imported for this function.
"""


def to_json_string(my_obj):
    """
    Function to return the JSON representation of an object.

    Args:
        my_obj: The object to be serialized.

    Returns:
        str: The JSON representation of the object.
    """
    return '"' + str(my_obj) + '"'
