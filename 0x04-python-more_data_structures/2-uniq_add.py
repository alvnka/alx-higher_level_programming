#!/usr/bin/python3

def uniq_add(my_list=[]):
    check_list = []
    result = 0
    for i in range(len(my_list)):
        if my_list[i] not in check_list:
            check_list.append(my_list[i])
    result = sum(map(lambda x: x, check_list))

    return (result)
