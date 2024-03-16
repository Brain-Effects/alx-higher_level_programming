#!/usr/bin/python3
"""
Module for MyInt class
"""

class MyInt(int):
    """
    MyInt class that inherits from int and inverts == and != operators
    """
    def __eq__(self, other):
        """
        Inverts == operator
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts != operator
        """
        return super().__eq__(other)
