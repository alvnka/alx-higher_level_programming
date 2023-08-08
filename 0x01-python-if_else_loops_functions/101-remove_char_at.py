#!/usr/bin/python3
def remove_char_at(str, n):
    new_string = ""
    index = 0
    for character in str:
        index = index + 1
        if index == n + 1:
            continue
        else:
            new_string = new_string + character
    return new_string
