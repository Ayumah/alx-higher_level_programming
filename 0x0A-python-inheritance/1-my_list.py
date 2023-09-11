#!/usr/bin/python3
"""
class MyList with method print_sorted
"""


class MyList(list):
    """MyList class that inherits from class list
    """

    def print_sorted(self):
        """ prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
