#!/usr/bin/python3
"""Module for find peak function"""

from typing import Sized


def find_peak(list_of_integers):
    """Finds a peak element using a binary search function.

    Doesn't take into account the first and last elements as peak
    """

    mid_idx = len(list_of_integers) // 2

    if len(list_of_integers) == 0 or list_of_integers is None:
        return None
    elif len(list_of_integers) < 3:
        return max(list_of_integers)
    else:
        if (list_of_integers[mid_idx] >= list_of_integers[mid_idx + 1] and
                list_of_integers[mid_idx] >= list_of_integers[mid_idx - 1]):
            return list_of_integers[mid_idx]
        elif (list_of_integers[mid_idx] < list_of_integers[mid_idx - 1]):
            return find_peak(list_of_integers[:mid_idx - 1])
        elif (list_of_integers[mid_idx] < list_of_integers[mid_idx + 1]):
            return find_peak(list_of_integers[mid_idx + 1:])
