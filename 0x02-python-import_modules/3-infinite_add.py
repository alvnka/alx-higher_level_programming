#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arguments = sys.argv
    sum = 0
    for index, argument in enumerate(arguments):
        if index == 0:
            continue
        else:
            sum = sum + int(argument)
    print("{}".format(sum))
