#!/usr/bin/python3
for i in range(00, 100):
    if i == 99:
        print(f"{i:02d}".format(), end="\n")
    else:
        print(f"{i:02d}".format(), end=", ")
