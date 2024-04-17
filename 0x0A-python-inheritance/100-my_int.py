#!/usr/bin/python3
"""overriding the eq and ne methods"""


class MyInt(int):
    """The class"""

    def __eq__(self, other):
        """return"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """return"""
        return not super().__ne__(other)
