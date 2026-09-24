def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    if len(a[0]) != len(b):
        return -1
        
    l = [] 
    for row in a:
        row_sum = 0
        for j in range(len(b)):
            k = row[j] * b[j]
            row_sum += k
        l.append(row_sum)
        
    return l