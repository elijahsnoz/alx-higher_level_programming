#!/usr/bin/python3
import random

# Generate a random number between -10000 and 10000
number = random.randint(-10000, 10000)

# Ensure the number is an integer
if not isinstance(number, int):
    print("Error: Wrong type")
else:
    # Determine the last digit of the number
    last_digit = abs(number) % 10

    # Output the last digit of the number and additional information based on its value
    print("Last digit of", number, "is", last_digit, end=" ")

    if last_digit > 5:
        print("and is greater than 5")
    elif last_digit == 0:
        print("and is 0")
    else:
        print("and is less than 6 and not 0")
