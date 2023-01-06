#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        while i < x:
            print(f"{my_list[i]}".format(), end="")
            i += 1
        print(f"")
        return (i)
    except LookupError:
        print(f"")
        return (i)
