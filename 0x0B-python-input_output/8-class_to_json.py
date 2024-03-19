#!/usr/bin/python3
"""
This module provides a function to convert an object's attributes
into a dictionary with simple data structures for JSON serialization.

Functions:
- class_to_json(obj): Returns the dictionary description with
simple data structure for JSON serialization of an object.

The function in this module takes an instance of a class as
input and returns a dictionary that represents the object's attributes.
The attributes are serialized into simple data structures: list,
dictionary, string, integer, and boolean. This function does not
handle exceptions if the object can't be serialized.
"""


def class_to_json(obj):
    """
    This function returns the dictionary description with simple
    data structure for JSON serialization of an object.

    Parameters:
    obj (object): An instance of a Class.

    Returns:
    dict: A dictionary that represents the obj with simple data structure.

    Note:
    All attributes of the obj Class are serializable: list,
    dictionary, string, integer and boolean.
    """
    return {key: value for key, value in obj.__dict__.items()
            if isinstance(value, (list, dict, str, int, bool))}
