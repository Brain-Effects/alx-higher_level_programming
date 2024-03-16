#!/usr/bin/python3
"""
This module contains a class BaseGeometry with public instance methods.
"""


class BaseGeometry:
    """
    This is a class named BaseGeometry that includes public instance methods.
    """

    def area(self):
        """
        This is a public instance method that raises an Exception
        with a message.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This is a public instance method that validates value.

        Args:
            name: The name of the value. Assumed to be a string.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
