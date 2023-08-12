#!/usr/bin/python3
def element_at(my_list, idx):
    return (None if ((idx < 0) or (idx + 1 > len(my_list))) else my_list[idx])
