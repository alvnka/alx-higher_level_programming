#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    if a_dictionary:
        for keys, values in a_dictionary.items():
            new_dict[keys] = values * 2
        return new_dict
    else:
        return a_dictionary
