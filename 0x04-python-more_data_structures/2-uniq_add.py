#!/usr/bin/python3
def uniq_add(my_list=[]):
    check_list = []
    if my_list:
        for item in my_list:
            if item not in check_list:
                check_list.append(item)
            else:
                continue
        return sum(map(lambda x: x, check_list))
    else:
        return 0
