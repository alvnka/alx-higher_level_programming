#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i+1, 10):
        if i != j:
            if i == 8 and j == 9:
                print(f"{i}{j}".format(), end="")
            else:
                print(f"{i}{j}".format(), end=", ")
