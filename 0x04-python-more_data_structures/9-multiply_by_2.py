#!/usr/bin/python3
def multiply_by_2(a_dictionary):
     new_dictionary = {}
    for i in a_dictionary:
         new_dictionary[i] = a_dictionary * 2
    return new_dictionary
