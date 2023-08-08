#!/usr/bin/python3

def uppercase(str):
    uppercase_string = ""
    for character in str:
        if (ord(character) >= 97 and ord(character) <= 122):
            uppercase_character = ord(character) - 32
            uppercase_string = uppercase_string + chr(uppercase_character)
        else:
            uppercase_character = character
            uppercase_string = uppercase_string + character

    print("{}".format(uppercase_string))
