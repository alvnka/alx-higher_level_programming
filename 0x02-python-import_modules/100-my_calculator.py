#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    arguments = sys.argv
    if (len(arguments) == 4):
        operators = ['+', '-', '*', '/']
        if arguments[2] not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            a = int(arguments[1])
            b = int(arguments[3])
            result = add(a, b) if (arguments[2] == '+') \
                else sub(a, b) if (arguments[2] == "-") \
                else mul(a, b) if (arguments[2] == '*') \
                else div(a, b) if (arguments[2] == '/') else None
            print("{0} {1} {2} = {3}".format(
                arguments[1], arguments[2], arguments[3], result))
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>".format())
        exit(1)
