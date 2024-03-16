#!/usr/bin/python3
class LockedClass:
    """
    LockedClass only allows creating the 'first_name' instance attribute.
    Attempting to create any other attribute will result in an AttributeError.
    """
    __slots__ = ['first_name']
