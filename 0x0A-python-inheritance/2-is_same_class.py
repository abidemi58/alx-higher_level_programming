#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class
    Args:
        - obj: object to look at
        - a_class: class to verify the instance of
    Returns: True if obj is an instance of a_class,
    False otherwise
    """

    return True if type(obj) is a_class else False
