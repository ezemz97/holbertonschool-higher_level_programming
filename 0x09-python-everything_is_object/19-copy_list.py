"""Function to copy a list"""


def copy_list(l):
    """Copy a list and return the new list

    Args:
        l (list): List to copy

    Returns:
        The new list

    Raises:
        TypeError: When the list is not list, or empty
    """
    if type(l) is not list:
        raise TypeError("Argument must be a list.")
    new_list = []
    new_list = l[:]
    return new_list

