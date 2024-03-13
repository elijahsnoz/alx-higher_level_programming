#!/usr/bin/python3
def fizzbuzz():
    """
    Prints numbers from 1 to 100 with replacements for multiples of three, five, and both.

    Returns:
        None
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")

# Call the function to print the FizzBuzz sequence
fizzbuzz()
