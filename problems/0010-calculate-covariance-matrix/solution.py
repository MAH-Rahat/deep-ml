def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    num_features = len(vectors)
    n = len(vectors[0])
    
    # Step 1: Calculate the mean for every feature list
    means = []
    for feature in vectors:
        means.append(sum(feature) / n)
        
    # Create an empty grid (matrix) to hold our final answers
    cov_matrix = [[0.0 for _ in range(num_features)] for _ in range(num_features)]
    
    # Step 2-4: Pair every feature with every other feature
    for i in range(num_features):
        for j in range(num_features):
            
            # Calculate the covariance for this specific pair
            covariance_sum = 0
            for k in range(n):
                diff_i = vectors[i][k] - means[i]
                diff_j = vectors[j][k] - means[j]
                covariance_sum += diff_i * diff_j
                
            # Divide by (n - 1) and drop it into the grid
            cov_matrix[i][j] = covariance_sum / (n - 1)
            
    return cov_matrix