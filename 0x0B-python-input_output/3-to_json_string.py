#!/usr/bin/python3


import json


"""
Module with function to_json_string
"""


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
