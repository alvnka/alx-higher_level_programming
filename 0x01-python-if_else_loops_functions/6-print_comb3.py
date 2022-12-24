#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i+1, 10):
        if i != j:
            if j > 1:
                print(f", ".format(), end="")
            print(f"{i}{j}".format(), end="")
print(f"\n".format())