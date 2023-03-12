#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if j < len(row) - 1:
                print(col, end=" ")
            else:
                print(col, end="")
        print()
