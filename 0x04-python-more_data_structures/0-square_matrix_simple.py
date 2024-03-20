#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix.

    Parameters:
    matrix (list): A 2D array representing the matrix.

    Returns:
    list: A new matrix with each value being the square of the corresponding value in the input matrix.
    """

    # Check if the matrix is empty
    if not matrix:
        return []

    # Initialize an empty list to store the squared values
    squared_matrix = []

    # Iterate over each row in the matrix
    for row in matrix:
        # Initialize an empty list to store the squared values of the current row
        squared_row = []
        # Iterate over each element in the row and compute its square
        for num in row:
            squared_row.append(num ** 2)
        # Add the squared row to the squared matrix
        squared_matrix.append(squared_row)

    return squared_matrix
