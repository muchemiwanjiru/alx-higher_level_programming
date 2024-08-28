def add_integer(a, b=98):
    """Function that adds two integers.

    Args:
        a: The first integer or float.
        b: The second integer or float, default is 98.

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is neither an integer nor a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)

