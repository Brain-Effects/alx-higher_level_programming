#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # Use the del statement to delete the key from the dictionary
    # If the key doesn't exist, catch the KeyError and do nothing
    try:
        del a_dictionary[key]
    except KeyError:
        pass

    # Return the updated dictionary
    return a_dictionary
