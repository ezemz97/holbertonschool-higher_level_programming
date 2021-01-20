"""Single function to write text to a file

Example: write_file("textfile.txt", "hello world")

"""


def write_file(filename="", text=""):
    """Write text to a file (UTF-8)

    Args:
        filename (str): Name of the file to open
        text (str): Text to write to the file

    Returns:
        Number of characters written

    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
