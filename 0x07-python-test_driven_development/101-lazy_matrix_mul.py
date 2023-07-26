#!/usr/bin/python3

"""Lazy matrix multiplication"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    # Convert input matrices to NumPy arrays
    m_a = np.array(m_a)
    m_b = np.array(m_b)

    # Perform matrix multiplication using NumPy
    try:
        result = np.dot(m_a, m_b)
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")

    # Convert the result back to a regular list of lists
    result = result.tolist()

    return result
