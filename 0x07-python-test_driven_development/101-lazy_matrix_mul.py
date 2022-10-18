#!/usr/bin/python3
"""Defines a function that multiplies 2 matrices by using the module NumPy"""
import numpy as res


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    return (res.matmul(m_a, m_b))
