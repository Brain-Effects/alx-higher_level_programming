#!/usr/bin/python3
class MyList(list):
    """
    This class inherits from the built-in list type and includes a method to print the list in ascending order.

    Methods:
    print_sorted: Prints the list in ascending order.
    """

    def print_sorted(self):
        """
        This method prints the list in ascending order.
        """
        print(sorted(self))
