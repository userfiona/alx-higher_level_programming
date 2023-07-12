#!/usr/bin/python3
"""
Module for pascal_triangle method.
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle.

    Args:
        n (int): Number of rows in the triangle.

    Returns:
        list: List of lists representing Pascal's triangle.
    """
    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)
        triangle.append(row)
    return triangle
