#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numbers = {
        'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50,
        'XC': 90, 'C': 100, 'CD': 400, 'D': 500,
        'CM': 900, 'M': 1000
    }
    result = 0
    while roman_string:
        if roman_string[:2] in roman_numbers:
            result += roman_numbers[roman_string[:2]]
            roman_string = roman_string[2:]
        else:
            result += roman_numbers[roman_string[0]]
            roman_string = roman_string[1:]

    return result
