#!/usr/bin/python3
# divisible_by_2 - finds all multiples pf 2 in a list

def divisible_by_2(my_list=[]):
    new_list = []
    for element in my_list:
        if element % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return (new_list)
