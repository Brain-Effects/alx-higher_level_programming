#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list
    new_list = []

    # Iterate over each element in the input list
    for element in my_list:
        # If element is the one to be replaced, add replacement to new list
        if element == search:
            new_list.append(replace)
        # Otherwise, add the original element to the new list
        else:
            new_list.append(element)

    # Return the new list
    return new_list
