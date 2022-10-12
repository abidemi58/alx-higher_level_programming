#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square.
    Private instance attribute: size.
    Instantiation with size (no type/value verification).
    """
    def __init__(self, size):
        """Initialize a new Square."""
        self.__size = size
