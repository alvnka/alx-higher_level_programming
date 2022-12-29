#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    to_sum = len(argv)
    result = 0
    i = 1
    for i in range(1, to_sum):
        result = result + int(argv[i])
    print(f"{result}".format())
