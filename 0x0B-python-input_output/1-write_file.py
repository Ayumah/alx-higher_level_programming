#!/usr/bin/python3
"""
module with function write_file
"""


def write_file(filename="", text=""):
    """
    write_file is a function writes a string to a text file
    (UTF8) and returns the number of characters written:
    """

    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
