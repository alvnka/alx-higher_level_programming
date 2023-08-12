#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    if matrix:
        for row in matrix:
            if row:
                for count, item in enumerate(row, 1):
                    if count < len(row):
                        print("{:d}" .format(item), end=' ')
                    else:
                        print("{:d}".format(item))
            else:
                print("")
    else:
        print("")
