#!/usr/bin/python3
"""
This module contains a function that returns the list of available attributes
and methods of an object.
"""

def lookup(obj):
    """
    This function returns a list of available attributes and
    methods of an object.

    Parameters:
    obj (object): The object whose attributes and methods are to be listed.

    Returns:
    list: A list of attributes and methods of the object.
    """

    return dir(obj)
