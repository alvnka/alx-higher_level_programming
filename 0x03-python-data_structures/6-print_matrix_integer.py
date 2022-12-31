#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) <= 1:
        print("".format())
    else:
        for column in range(3):
            for row in range(3):
                print(f"{matrix[column][row]}".format(), end="")
                if row < 2:
                    print(" ".format(), end="")
            print("".format())
