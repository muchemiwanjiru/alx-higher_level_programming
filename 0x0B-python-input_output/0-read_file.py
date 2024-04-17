#!/usr/bin/python3
"""Read file function"""


def read_file(filename=""):
    """prints"""

    with open(filename, "r", encoding="utf8") as f:
        print(f.read())
