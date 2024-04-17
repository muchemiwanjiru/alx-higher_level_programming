#!/usr/bin/python3
"""appends to file"""


def append_write(filename="", text=""):
    """implimentation"""
    with open(filename, "a", encoding="utf8") as f:
        appended = f.write(text)
        return appended
