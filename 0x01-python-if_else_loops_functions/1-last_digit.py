#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number >= 0:
    remainder = number % 10
    if remainder > 5:
        print(f"Last digit of {number} is {remainder} and is greater than 5")
    elif remainder == 0:
        print(f"Last digit of {number} is {remainder} and is 0")
    elif remainder < 6 and remainder != 0:
        print(
            f"Last digit of {number} is {remainder}"
            " and is less than 6 and not 0")
elif number < 0:
    remainder = ((number % 10) - 10)
    if remainder == -10:
        remainder = 0
    if remainder > 5:
        print(f"Last digit of {number} is {remainder} and is greater than 5")
    elif remainder == 0:
        print(f"Last digit of {number} is {remainder} and is 0")
    elif remainder < 6 and remainder != 0:
        print(
            f"Last digit of {number} is {remainder} "
            "and is less than 6 and not 0")
