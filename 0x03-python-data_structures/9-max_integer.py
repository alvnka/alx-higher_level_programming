#!/usr/bin/python3
# max_integer - find the biggest integer of a list

def max_integer(my_list=[]):
    if len(my_list) <= 0:
        return (None)
    else:
        large_element = 0
        for element in my_list:
            if element > large_element:
                large_element = element
    return (large_element)
