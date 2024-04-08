#!/usr/bin/python3
import sys
"""a program that solves the N queens problem
        The N queens puzzle is the challenge of placing
        N non-attacking queens on an N×N chessboard.
"""


def intable(s):
    """_summary_

    Args:
        s (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        return int(s)
    except ValueError:
        print("N must be a number")
    exit(1)


def queen():
    arg_arr = sys.argv

    if len(arg_arr) != 2:
        print("Usage: nqueens N")
        exit(1)

    n = intable(arg_arr[1])
    if not isinstance(n, int):
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)
    print(n)


if __name__ == "__main__":
    queen()
