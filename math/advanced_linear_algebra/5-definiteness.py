#!/usr/bin/env python3
"""Module for calculating matrix definiteness."""
import numpy as np


def definiteness(matrix):
    """Calculates the definiteness of a matrix.

    Args:
        matrix (numpy.ndarray): A square matrix of shape (n, n).

    Raises:
        TypeError: If matrix is not a numpy.ndarray.

    Returns:
        str: A string describing the definiteness, or None if invalid.
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    # Check if matrix is valid (2D, square, non-empty)
    if matrix.size == 0 or len(matrix.shape) != 2:
        return None

    n = matrix.shape[0]
    if matrix.shape[1] != n or n == 0:
        return None

    # Calculate eigenvalues
    eigenvalues = np.linalg.eigvals(matrix)

    # Check for complex eigenvalues (indicates non-symmetric matrix)
    if np.any(np.iscomplex(eigenvalues)):
        return None

    # Make eigenvalues real (ignore negligible imaginary parts)
    eigenvalues = np.real(eigenvalues)

    # Use a small tolerance for numerical stability
    tol = 1e-10

    # Count positive, negative, and near-zero eigenvalues
    positive = np.sum(eigenvalues > tol)
    negative = np.sum(eigenvalues < -tol)
    zero = np.sum(np.abs(eigenvalues) <= tol)

    # Determine definiteness
    if negative == 0 and positive == n:
        return "Positive definite"
    elif negative == 0 and positive > 0 and zero > 0:
        return "Positive semi-definite"
    elif positive == 0 and negative == n:
        return "Negative definite"
    elif positive == 0 and negative > 0 and zero > 0:
        return "Negative semi-definite"
    elif positive > 0 and negative > 0:
        return "Indefinite"

    return None
