#!/usr/bin/env python3
"""Module for calculating matrix definiteness."""
import numpy as np


def definiteness(matrix):
    """Calculates the definiteness of a matrix.

    Args:
        matrix (numpy.ndarray): A square matrix of shape (n, n).

    Returns:
        str: A string describing the definiteness.
    """
    if not isinstance(matrix, np.ndarray):
        return "matrix must be a numpy.ndarray"

    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        return "matrix must be a square matrix"

    if matrix.size == 0:
        return "matrix must be a square matrix"

    if not np.allclose(matrix, matrix.T):
        return "matrix must be symmetric"

    eigenvalues = np.linalg.eigvals(matrix)
    eigenvalues = np.real(eigenvalues)

    tol = 1e-10

    positive = np.sum(eigenvalues > tol)
    negative = np.sum(eigenvalues < -tol)
    zero = np.sum(np.abs(eigenvalues) <= tol)
    n = matrix.shape[0]

    if positive == n:
        return "Positive definite"
    if positive > 0 and zero > 0 and negative == 0:
        return "Positive semi-definite"
    if negative == n:
        return "Negative definite"
    if negative > 0 and zero > 0 and positive == 0:
        return "Negative semi-definite"
    if positive > 0 and negative > 0:
        return "Indefinite"

    return None
