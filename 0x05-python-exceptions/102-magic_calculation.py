#!/usr/bin/python3


def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
    """
    A function that prints an integer with
    "{:d}".format()
    """
        try:
            if i > a:
                raise Exception("Too far")
            else:
                result += (a ** b) / i
        except:
            result = b + a
            break
    return result
