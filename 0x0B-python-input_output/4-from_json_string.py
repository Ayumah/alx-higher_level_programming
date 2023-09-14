#!/usr/bin/python3
import json
"""
Module with function from_json_string
"""


def from_json_string(my_str):
    """ function that returns an Python data represented by a JSON """
    return json.loads(my_str)
