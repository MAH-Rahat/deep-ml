def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    # Extract the variables [a, b] and [c, d]
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    
    # Calculate the determinant (ad - bc)
    det = (a * d) - (b * c)
    
    # Return None if not invertible
    if det == 0:
        return None
        
    # Apply the inverse formula
    return [
        [d / det, -b / det],
        [-c / det, a / det]
    ]