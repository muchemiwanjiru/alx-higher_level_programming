#!/usr/bin/python3
"""find max int module"""


def max_integer(list=[]):
    """Function to find max value """

    if len(list) == 0:
        return None
    list_value = list[0]
    i = 1
    while i < len(list):
        if list[i] > list_value:
            list_value = list[i]
        i += 1
    return list_value
