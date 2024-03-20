#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    Returns a set of common elements in two sets.

    Parameters:
    set_1 (set): The first set.
    set_2 (set): The second set.

    Returns:
    set: A set containing common elements found in both sets.
    """
    # Initialize an empty set to store common elements
    common_set = set()

    # Iterate through each element in set_1
    for element in set_1:
        # If the element is also in set_2, add it to the common_set
        if element in set_2:
            common_set.add(element)

    return common_set
