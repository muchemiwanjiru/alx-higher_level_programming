#!/usr/bin/python3
# 101-locked_class.py

"""class defined is for locked class"""


class LockedClass:
    """
    the class prevents any user from instantiating  any new LockedClass attribute other than 'first_name'.
    """

    __slots__ = ["first_name"]
