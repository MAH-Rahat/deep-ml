def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means = []
    
    if mode == "row":
        for row in matrix:
            means.append(sum(row) / len(row))
            
    elif mode == "column":
        for i in range(len(matrix[0])):
            col = []
            for row in matrix:
                col.append(row[i])
            means.append(sum(col) / len(col))
            
    return means