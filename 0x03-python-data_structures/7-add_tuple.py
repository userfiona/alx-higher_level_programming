#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Computes the element-wise sum of two tuples.

    Args:
        tuple_a: The first input tuple.
        tuple_b: The second input tuple.

    Returns:
        A new tuple containing the element-wise sum of tuple_a and tuple_b.
    """
    new_tuple = ()
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    new_tuple = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return new_tuple
