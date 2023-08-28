#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    try:
        result = fct(*args)
        print("{:d}".format(result))
        return True
    except Exception as err:
        sys.stderr.write(f"Exception: {err}\n")
        return None
