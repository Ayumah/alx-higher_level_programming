#!/usr/bin/python3
"""
read_line is a function a function that reads a text file 
(UTF8) and prints it to stdout:
"""

def read_file(filename=""):
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
