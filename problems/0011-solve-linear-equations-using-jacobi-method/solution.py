import numpy as np

def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    # Initialize the solution vector to all zeros
    x = np.zeros(len(b))
    
    # Extract the diagonal values and the remaining off-diagonal values
    D = np.diag(A)
    R = A - np.diag(D)
    
    # Update the guess exactly n times
    for _ in range(n):
        x = (b - np.dot(R, x)) / D
        
    # Round to 4 decimal places and return as a standard Python list
    return np.round(x, 4).tolist()