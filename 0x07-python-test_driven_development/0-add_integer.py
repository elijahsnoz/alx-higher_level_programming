#!/usr/bin/python3
def add_integer(a, b=98):
    # Check if a and b are integers or floats
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    
    # Cast a and b to integers if they are floats
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    
    # Return the addition of a and b
    return int(a + b)

# Test the function
print(add_integer(5, 3))  # Output: 8
print(add_integer(5.5, 3))  # Output: 8
print(add_integer(5, 3.5))  # Output: 8
print(add_integer(5.5, 3.5))  # Output: 8
