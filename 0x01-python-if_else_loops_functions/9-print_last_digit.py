#!/usr/bin/python3
def print_last_digit(number):
    """
    Prints the last digit of a number and returns its value.

    Args:
        number: An integer number.

    Returns:
        The value of the last digit.
    """
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
