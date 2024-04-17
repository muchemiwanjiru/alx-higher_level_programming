#!/usr/bin/python3
"""contains the MyList class"""
class MyList(list):

    """list subclass"""
    def print_sorted(self):

        sorted_list = sorted(self)

        """printing"""
        print(sorted_list)
