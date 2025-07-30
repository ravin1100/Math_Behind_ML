"""
mlmath - A simple math library for machine learning-related operations.
"""

from typing import List, Dict

def dot_product(a: List[float], b: List[float]) -> float:
    """
    Compute the dot product of two vectors.

    Parameters:
    a (List[float]): First vector.
    b (List[float]): Second vector.

    Returns:
    float: Dot product result.

    Example:
    >>> dot_product([1, 2, 3], [4, 5, 6])
    32
    """
    if len(a) != len(b):
        raise ValueError("Vectors must be of same length.")
    return sum(x * y for x, y in zip(a, b))


def matrix_multiply(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    """
    Multiply two matrices A and B.

    Parameters:
    A (List[List[float]]): First matrix (m x n).
    B (List[List[float]]): Second matrix (n x p).

    Returns:
    List[List[float]]: Resultant matrix (m x p).

    Example:
    >>> matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    [[19, 22], [43, 50]]
    """
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must equal number of rows in B.")

    result = []
    for row in A:
        new_row = []
        for col in zip(*B):
            new_row.append(dot_product(row, list(col)))
        result.append(new_row)
    return result


def conditional_probability(events: Dict[str, int]) -> float:
    """
    Calculate conditional probability P(A|B) using counts.

    Parameters:
    events (Dict[str, int]):
        Dictionary with keys:
        - 'A_and_B': count of both A and B occurring
        - 'B': count of B occurring

    Returns:
    float: P(A|B)

    Example:
    >>> conditional_probability({'A_and_B': 120, 'B': 400})
    0.3
    """
    A_and_B = events.get('A_and_B')
    B = events.get('B')

    if B == 0:
        raise ValueError("Probability denominator (B) cannot be zero.")
    return A_and_B / B
