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

    whitespace = False
    for character in text:
        if (
            character is not "." and character is not ":"
            and character is not "?"
        ):
            if whitespace is False:
                print("{}".format(character), end="")
            else:
                whitespace = False
                continue
        else:
            print("{}".format(character))
            print()
            whitespace = True
