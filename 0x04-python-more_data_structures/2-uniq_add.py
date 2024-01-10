#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create a set from the list to remove duplicates
    unique_set = set(my_list)

    # Sum all the unique integers in the set
    sum_unique = sum(unique_set)

    # Return the sum
    return sum_unique
