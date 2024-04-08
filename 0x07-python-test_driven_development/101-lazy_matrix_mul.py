#!/usr/bin/python3

"""importing numpy module"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """function to print lazy matrix"""
    try:
        matrix_result = np.dot(m_a, m_b)
        return matrix_result
    except ValueError:
        raise ValueError("Matrices are not compatible for multiplication")
