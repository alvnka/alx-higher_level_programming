#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = (number % 10) if number > 0 else 0 if (
    number % 10 == 0) else (-10 + (number % 10))
state = None if last_digit == 0 else 1 if last_digit > 5 else 0
print("Last digit of {} is {} and is less than 6 and not 0"
      .format(number, last_digit) if state == 0
      else "Last digit of {} is {} and is greater than 5"
      .format(number, last_digit) if state == 1
      else "Last digit of {} is {} and is 0"
      .format(number, last_digit))
