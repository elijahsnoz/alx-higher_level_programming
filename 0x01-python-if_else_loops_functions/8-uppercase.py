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
        # Check if the character is a lowercase letter
        if ord('a') <= ord(char) <= ord('z'):
            # Convert the lowercase letter to uppercase using ASCII values
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char
        print(uppercase_char, end="")
    print()

# Test cases
uppercase("best")
uppercase("Best School 98 Battery street")
