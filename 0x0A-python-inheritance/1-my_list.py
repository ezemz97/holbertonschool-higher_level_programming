#!/usr/bin/python3
"""Defines a class MyList with a method to print a sorted list"""


class MyList(list):
    """Defines the class MyList"""
    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self))
