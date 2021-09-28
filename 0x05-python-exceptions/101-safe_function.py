#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except (ZeroDivisionError, TypeError, IndexError) as err:
        print("Exception:", err, file=sys.stderr)
        result = None
    return result
