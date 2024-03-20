#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Parameters:
    my_list (list): The initial list.
    """
    # Create a new list to store the modified elements
    new_list = []
    for item in my_list:
        # If the element matches the 'search' element, replace it with the 'replace' element
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
    return new_list

