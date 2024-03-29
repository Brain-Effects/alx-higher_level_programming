#!/usr/bin/python3
def best_score(a_dictionary):
    # Check if the dictionary is empty
    if not a_dictionary:
        return None

    # Find the key with the biggest value
    max_key = max(a_dictionary, key=a_dictionary.get)

    # Return the key with the biggest value
    return max_key
