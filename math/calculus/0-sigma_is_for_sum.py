#!/usr/bin/env python3
"""
Compute the summation Σ from i=2 to 5
"""

def sigma_sum(start: int, end: int) -> int:
    """Return the sum of integers from start to end inclusive."""
    return sum(range(start, end + 1))

if __name__ == "__main__":
    result = sigma_sum(2, 5)
    print(result)  # Expected output: 14
