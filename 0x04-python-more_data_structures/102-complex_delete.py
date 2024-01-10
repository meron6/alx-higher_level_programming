#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev = 0
    for char in roman_string:
        if char not in roman_dict:
            return 0
        curr = roman_dict[char]
        if prev < curr:
            result -= prev
        else:
            result += prev
        prev = curr
    result += prev
    if result < 1 or result > 3999:
        return 0
    return result
