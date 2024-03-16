#!/usr/bin/python3
"""
Module for add_attribute function
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if it's possible

    Parameters:
    obj: The object to add the attribute to
    attr: The name of the attribute to add
    value: The value of the attribute to add

    Returns:
    None

    Raises:
    TypeError: If the object can't have new attributes
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
