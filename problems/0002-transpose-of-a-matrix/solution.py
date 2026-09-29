def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    y = [] 
    for i in range(len(a[0])):
        new_row = []
        
        for j in a:
             new_row.append(j[i])
        
        y.append(new_row)
        
    return y