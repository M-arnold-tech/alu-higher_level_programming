#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Iterate over each row in the matrix
    for row in matrix:
        # Use str.format() to print each integer in the row, joined by spaces
        print(" ".join("{:d}".format(num) for num in row))
