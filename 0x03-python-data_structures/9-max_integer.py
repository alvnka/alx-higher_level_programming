#!/usr/bin/python3

def max_integer(my_list=[]):
    largest_int = my_list[0] if my_list[0] < 0 else 0
    if my_list:
        for number in my_list:
            largest_int = number if largest_int < number else largest_int
        return largest_int
    else:
        return None
