#!/user/bin/python3
def add_integer(a, b=98):
    """
    This function adds two numbers together.

    Parameters:
    a (int, float): The first number to add. Must be an integeror float.
    b (int, float): The second number to add. Must be an integer or float.
    Defaults to 98

    Returns:
    int: The sum of a and b, cast to an integer.

    Raises:
    TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
