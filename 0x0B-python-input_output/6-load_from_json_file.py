#!/usr/bin/python3
"""
Module with function load_from_json
"""


import json


def load_from_json_file(filename):
    """ function that creates an object from JSON file"""


    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
