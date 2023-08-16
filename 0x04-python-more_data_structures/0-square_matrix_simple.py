#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    if matrix:
        for count_row, row in enumerate(matrix):
            new_rows = []
            for count, item in enumerate(row):
                new_rows.append(item ** 2)
            new_matrix.append(new_rows)
        return new_matrix
    else:
        return matrix
