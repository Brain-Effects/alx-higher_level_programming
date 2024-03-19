#!/usr/bin/python3
def class_to_json(obj):
    """
    This function returns the dictionary description with simple
    data structure for JSON serialization of an object.

    Parameters:
    obj (object): An instance of a Class.

    Returns:
    dict: A dictionary that represents the obj with simple data structure.

    Note:
    All attributes of the obj Class are serializable: list,
    dictionary, string, integer and boolean.
    """
    return {key: value for key, value in obj.__dict__.items()
            if isinstance(value, (list, dict, str, int, bool))}
