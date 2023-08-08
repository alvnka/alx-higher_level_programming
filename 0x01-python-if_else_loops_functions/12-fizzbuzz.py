#!/usr/bin/python3

def fizzbuzz():
    for number in range(1, 101):
        output = "Fizz" if (number % 3 == 0) else "Buzz" if (
            number % 5 == 0) else number
        print("{} ".format(output), end= '')
