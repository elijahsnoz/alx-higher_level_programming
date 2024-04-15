#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Check if `obj` is an instance of a class that inherited (directly or indirectly)
    from the specified class `a_class`.
    
    Args:
    - obj: The object to check.
    - a_class: The class to check against.

    Returns:
    - True if `obj` is an instance of a subclass of `a_class`, otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
