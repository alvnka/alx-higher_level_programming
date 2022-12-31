#!/usr/bin/python3
# multiple return - function that returns a tuple with
#   the length of a string and it's first character

def multiple_returns(sentence):
    if len(sentence) < 1:
        ret_tuple = (0, None)
        return (ret_tuple)
    else:
        length = len(sentence)
        character1 = sentence[0]
        ret_tuple = (length, character1)
        return (ret_tuple)
