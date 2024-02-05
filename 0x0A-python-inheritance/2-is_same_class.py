#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    This function checks if an object is exactly an instance
    of the specified class.

    Parameters:
    obj (object): The object to check.
    a_class (class): The class to check against.

    Returns:
    bool: True if the object is exactly an instance of the specified class,
    otherwise False.
    """
    return type(obj) is a_class
