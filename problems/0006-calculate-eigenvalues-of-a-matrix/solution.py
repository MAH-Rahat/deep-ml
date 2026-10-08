def calculate_eigenvalues(matrix: list[list[float]]) -> list[float]:
    det_A = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    trace_A = matrix[0][0] + matrix[1][1]
    
    inner_part = (trace_A ** 2) - (4 * det_A)
    
    l1 = (trace_A + inner_part ** 0.5) / 2
    l2 = (trace_A - inner_part ** 0.5) / 2
    
    return [max(l1, l2), min(l1, l2)]