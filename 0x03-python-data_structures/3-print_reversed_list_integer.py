#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    index = -1
    while index >= (-1 * (len(my_list))):
        print("{:d}".format(my_list[index]))
        index -= 1