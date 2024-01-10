#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Get the keys of the dictionary and sort them
    sorted_keys = sorted(a_dictionary.keys())

    # Iterate over each key in the sorted list of keys
    for key in sorted_keys:
        # Print the key and its corresponding value
        print("{}: {}".format(key, a_dictionary[key]))
