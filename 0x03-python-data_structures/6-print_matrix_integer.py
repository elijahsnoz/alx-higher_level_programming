#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print("Empty matrix")
        return
    for row in matrix:
        if not row:
            print("Empty row")
            continue
        for num in row:
            print("{:d}".format(num), end=" ")
        print()
