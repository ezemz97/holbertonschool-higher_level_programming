#!/usr/bin/python3
"""Single function module:
This function prints text with 2 new lines,
after a colon, a period or a question mark

"""


def text_indentation(text):
    """Prints text followed by a new line, and
    adds another new line after a colon, a period
    or a question mark

    Args:
        text (str): Text to parse

    Raises:
        TypeError: if 'text' is not a string

    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    white = 0
    for char in text:
        if white == 1:
            if char == " ":
                continue
            else:
                white = 0
        if char == "?" or char == "." or char == ":":
            print(char)
            white = 1
        else:
            print(char, end="")
