#!/usr/bin/python3
import random
number = random.randint(-10, 10)

print("{0} is zero".format(number) if number == 0
      else "{0} is negative".format(number) if number < 0
      else "{0} is positive".format(number))
