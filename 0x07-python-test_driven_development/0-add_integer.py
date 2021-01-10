#!/usr/bin/python3
"""A single function module,
the function adds two numbers

"""
def add_integer(a, b=98):
    """This function sums two numbers

    Args:
        a (int)(float): First number to add
        b (int)(float): Second number to add
    
    Returns:
        The product of a + b
    
    Raises:
        TypeError if arguments not (int) or (float)
    
    """
    if isinstance(a, bool):
        a = "hello darkness"
    if isinstance(b, bool):
        b = "my old friend"
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
