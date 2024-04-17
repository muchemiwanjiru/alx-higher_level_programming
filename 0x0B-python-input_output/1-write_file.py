#!/usr/bin/python3
"""wites a string to txt file"""


def write_file(filename="", text=""):
    """it writes text to file"""

    with open(filename, "w", encoding="utf8") as f:
        written = f.write(text)
        return written
