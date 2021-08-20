#!/usr/bin/python3
"""Module for find peak function"""


def find_peak(list_of_integers):
    """Finds a peak element using a binary search function.

    Doesn't take into account the first and last elements as peak
    """

    if len(list_of_integers) == 0 or list_of_integers is None:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        return max(list_of_integers)
    else:
        mid_idx = int(len(list_of_integers) // 2)
        if (list_of_integers[mid_idx] >= list_of_integers[mid_idx + 1] and
                list_of_integers[mid_idx] >= list_of_integers[mid_idx - 1]):
            return list_of_integers[mid_idx]
        elif (list_of_integers[mid_idx] < list_of_integers[mid_idx + 1]):
            return find_peak(list_of_integers[mid_idx + 1:])
        elif (list_of_integers[mid_idx] < list_of_integers[mid_idx - 1]):
            return find_peak(list_of_integers[:mid_idx - 1])
