def add_integer(a, b=98):
    """
    Adds two integers or floats and returns an integer result.

    Parameters:
    a (int, float): The first number.
    b (int, float, optional): The second number. Defaults to 98.

    Returns:
    int: The sum of `a` and `b`.

    Raises:
    TypeError: If `a` or `b` is neither an integer nor a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)

