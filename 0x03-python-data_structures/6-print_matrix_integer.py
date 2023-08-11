#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    if len(matrix) != 0:
        for row in matrix:
            if len(row) != 0:
                for count, item in enumerate(row, 1):
                    if count < len(row):
                        print("{}" .format(item), end=' ')
                    else:
                        print("{}".format(item))
            else:
                print("")
    else:
        print("it was null".format())
