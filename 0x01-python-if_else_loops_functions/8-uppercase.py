#!/usr/bin/python3
def uppercase(str):
    result = ''
    for i in str:
        if i.isnumeric():
            result += i
        elif ord(i) >= 65 and ord(i) <= 90 :
            result += chr(ord(i))
        elif ord(i) >= 97 and ord(i) <= 122:
            result += chr(ord(i) - 32)
        else:
            result += i
    print(f"{result}".format())