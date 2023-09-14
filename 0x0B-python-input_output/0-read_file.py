#!/usr/bin/python3
"""
module with function read_line
"""

def read_file(filename=""):
    """
    read_line is a function a function that reads a text file
    (UTF8) and prints it to stdout:
    """

    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
