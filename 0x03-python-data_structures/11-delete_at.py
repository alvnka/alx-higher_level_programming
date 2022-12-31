#!/usr/bin/python3
# delete_at -  function to delete item at a specific position on the list

def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        del my_list[idx]
        return (my_list)
    else:
        return (my_list)
