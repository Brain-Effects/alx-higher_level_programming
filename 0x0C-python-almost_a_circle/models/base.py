#!/usr/bin/python3
"""
This is the "base" module.

This module provides the base for all other classes in the project.
The goal of it is to manage the id attribute in all future classes
and to avoid duplicating the same code (by extension, same bugs).
"""
import json


class Base:
    """
    This is the Base class.

    This class serves as the base for all other classes in the project.
    It manages the id attribute in all future classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is the constructor method for the Base class.

        If id is provided, it is assigned to the public instance attribute id.
        If id is not provided, __nb_objects is incremented and its
        new value is assigned to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This static method returns the JSON string representation of
        list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
