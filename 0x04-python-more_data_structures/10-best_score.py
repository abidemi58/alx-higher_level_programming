#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    num = list(a_dictionary.keys())[0]
    item = a_dictionary[num]
    for i and j in a_dictionary.items():
        if j > item:
            item = j
            num = i
    return num
