def add_vectors(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must be of the same length")
    return [a + b for a, b in zip(v1, v2)]

def dot_product(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must be of the same length")
    return sum(a * b for a, b in zip(v1, v2))

def are_orthogonal(v1, v2):
    return dot_product(v1, v2) == 0


