import numpy as np

def transform_matrix(A: list[list[float]], T: list[list[float]], S: list[list[float]]) -> list[list[float]] | int:
    A_arr = np.array(A)
    T_arr = np.array(T)
    S_arr = np.array(S)
    
    if np.linalg.det(T_arr) == 0 or np.linalg.det(S_arr) == 0:
        return -1
        
    T_inv = np.linalg.inv(T_arr)
    result = T_inv @ A_arr @ S_arr
    
    return result.tolist()