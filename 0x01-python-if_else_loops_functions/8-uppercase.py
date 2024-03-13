#!/usr/bin/python3
def uppercase(s):
    """
    Prints a string in uppercase followed by a new line.

    Args:
        s: The input string.

    Returns:
        None
    """
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char
        print("{}".format(uppercase_char), end="")
    print()
