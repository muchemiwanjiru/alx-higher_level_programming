#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    """ function to print maximum multiplication"""

    """ Validating m_a and m_b """
    for m in (m_a, m_b):
        if not isinstance(m, list):
            raise TypeError("m_a must be a list or m_b must be a list")
        if not all(isinstance(row, list) for row in m):
            raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
        if not m:
            raise ValueError("m_a can't be empty or m_b can't be empty")
        if not all(isinstance(val, (int, float)) for row in m for val in row):
            raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")
        if not all(len(row) == len(m[0]) for row in m):
            raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    """checking multiplication"""
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    """ Multipling m_a and m_b """
    mul_result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            mul_val = 0
            for k in range(len(m_b)):
                mul_val += m_a[i][k] * m_b[k][j]
            row.append(mul_val)
        mul_result.append(row)
    return mul_result
