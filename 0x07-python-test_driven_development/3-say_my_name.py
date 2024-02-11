#!/usr/bin/python3


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>.

    Args:
        first_name (str): The first name of the person.
        last_name (str, optional): The last name of the person. Defaults to "".

    Raises:
        TypeError: If first_name or last_name is not a string.
    """

    # Check if first_name and last_name are strings
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the name
    print("My name is {} {}".format(first_name, last_name))
