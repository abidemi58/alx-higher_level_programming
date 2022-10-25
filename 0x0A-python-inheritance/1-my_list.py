#!/usr/bin/python3
"""Creates a class inheriting from the list class.
"""


class MyList(list):
    """Class MyList inherits from list."""

    def print_sorted(self):
        """Prints the list, in ascending sort."""
        print(sorted(self))
