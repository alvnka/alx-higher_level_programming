#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    i = 1
    if length - 1 == 0:
        print(f"{length - 1} arguments.".format())
    elif length - 1 == 1:
        print(f"{length - 1} argument:".format())
    elif length - 1 > 1:
        print(f"{length - 1} arguments:".format())
    while i < length:
        print(f"{i}: {argv[i]}".format())
        i += 1
