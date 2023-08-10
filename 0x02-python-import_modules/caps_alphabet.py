#!/usr/bin/python3
if __import__ != "__main__":
    for alphabet in range(65, 91):
        print("{}".format(chr(alphabet)), end='') if alphabet < 90 else print(
            "{}".format(chr(alphabet)))
