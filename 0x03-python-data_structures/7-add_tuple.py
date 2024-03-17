#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Extracting the first two elements of each tuple, if available, else defaulting to 0
    a = tuple_a[:2] + (0,) * (2 - len(tuple_a))
    b = tuple_b[:2] + (0,) * (2 - len(tuple_b))
    result = (a[0] + b[0], a[1] + b[1])
    return result
