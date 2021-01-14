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
        raise TypeError("text must be a string")

    white = False
    for char in text:
        if char is " ":
            if white is True:
                continue
            else:
                print("{}".format(char), end="")
                white = True
        elif char is ":" or char is "." or char is "?":
            print("{}".format(char), end="\n")
            white = True
        else:
            print("{}".format(char), end="")
            white = False











    '''
    whitespace = False
    for char in text:
        if (
            char is not "." and char is not ":"
            and char is not "?"
        ):
            if whitespace is False:
                print("{}".format(char), end="")
            elif whitespace is True and char is " ":
                whitespace = False
                continue
        else:
            print("{}".format(char))
            print()
            whitespace = True
    '''