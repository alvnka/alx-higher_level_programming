#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for column in range(3):
        new_matrix.append([])
        for row in range(3):
            new_matrix[column].append(
                matrix[column][row] * matrix[column][row])
    return (new_matrix)
