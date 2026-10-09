def matrixmul(a: list[list[int|float]], b: list[list[int|float]]) -> list[list[int|float]] | int:
    # Return -1 if shapes don't align (columns of A must equal rows of B)
    if len(a[0]) != len(b):
        return -1
        
    c = []
    
    # Iterate through rows of A
    for i in range(len(a)):
        new_row = []
        
        # Iterate through columns of B
        for j in range(len(b[0])):
            dot_product = 0
            
            # Calculate the dot product for the current row/column pair
            for k in range(len(b)):
                dot_product += a[i][k] * b[k][j]
                
            new_row.append(dot_product)
            
        c.append(new_row)
        
    return c