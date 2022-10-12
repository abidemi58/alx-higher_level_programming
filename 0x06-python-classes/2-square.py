#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represents a square.
    Private instance attribute: size.
    Instantiation with optional size.
    """
    def __init__(self, size=0):
        """Initializes a new Square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
