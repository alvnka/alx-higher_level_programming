#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arguments = sys.argv
    print("{} arguments.".format(len(arguments) - 1)) \
        if len(arguments) == 1 \
        else print("{} argument:".format(len(arguments)-1)) \
        if len(arguments) == 2 \
        else print("{} arguments:".format(len(arguments)-1))
    for index, argument in enumerate(arguments):
        if index == 0:
            continue
        else:
            print("{}: {}".format(index, argument))
