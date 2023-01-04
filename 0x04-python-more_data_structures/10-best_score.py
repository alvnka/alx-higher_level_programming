#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        largestValue = 0
        largestKey = None
        for Key, values in a_dictionary.items():
            if values > largestValue:
                largestValue = values
                largestKey = Key
        return (largestKey)
    else:
        return (None)
