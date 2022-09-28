#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    for i in range(len(roman_string)):
        if roman_dict.get(roman_string[i], 0) == 0:
            return (0)

        if (i != (len(roman_string) - 1) and
                roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]):
                num += roman_dict[roman_string[i]] * -1

        else:
            num += roman_dict[roman_string[i]]
    return (num)
