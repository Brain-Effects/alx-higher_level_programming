#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list.

    Args:
        my_list (list): The list to print. Can contain any type (integer, string, etc.)
        x (int): The number of elements to print. Can be bigger than the length of my_list.

    Returns:
        int: The real number of elements printed.
    """
    num_printed = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            num_printed += 1
        except IndexError:
            break
    print()
    return num_printed
