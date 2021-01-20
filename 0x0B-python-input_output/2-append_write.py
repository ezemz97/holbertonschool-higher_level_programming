#!/usr/bin/python3
"""Single function to write text to a file

Example: append_write("textfile.txt", "hello world")

"""


def append_write(filename="", text=""):
    """Append text to a file (UTF-8)

    Args:
        filename (str): Name of the file to open
        text (str): Text to write to the file

    Returns:
        Number of characters added

    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
