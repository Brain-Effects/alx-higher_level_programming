#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Use the assignment operator to add the key/value pair to the dictionary
    # If the key already exists, its value will be replaced
    # If the key doesn't exist, it will be created
    a_dictionary[key] = value

    # Return the updated dictionary
    return a_dictionary
