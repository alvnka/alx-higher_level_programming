def fizzbuzz():
    for i in range(1,101,1):
        if ((i % 3) == (i % 5) == 0):
            print(f"FizzBuzz".format(), end="")
        elif i % 3 == 0:
            print(f"Fizz".format(), end="")
        elif i % 5 == 0:
            print(f"Buzz".format(), end="")
        else:
            print(f"{i}".format(), end="")
        print(f" ".format(), end = "")