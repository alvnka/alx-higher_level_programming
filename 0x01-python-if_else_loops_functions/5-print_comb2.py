#!/usr/bin/python3
for i in range(00, 100):
    if i > 0:
        print(", ".format(), end="")
    print(f"{i:02d}".format(), end="")
