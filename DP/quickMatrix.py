def matrix_chain_order(d):
    """
    Calculate the minimum cost of matrix chain multiplication and the optimal parenthesization.
    learnt from chatgpt
    :param d: Dimensions of the matrix chain, length is n+1 (represents n matrices).
    :return: Minimum cost matrix M and split point matrix S.
    """
    n = len(d) - 1  # Number of matrices
    M = [[0] * n for _ in range(n)]  # Stores the minimum multiplication costs
    S = [[0] * n for _ in range(n)]  # Stores the split points

    # gap represents the length of the matrix chain - 1
    for gap in range(1, n):  # gap ranges from 1 to n-1
        for i in range(n - gap):
            j = i + gap
            M[i][j] = float('inf')  # Initialize to positive infinity
            for k in range(i, j):  # Try all possible split points k
                # Calculate the cost for split point k
                cost = M[i][k] + M[k + 1][j] + d[i] * d[k + 1] * d[j + 1]
                if cost < M[i][j]:
                    M[i][j] = cost
                    S[i][j] = k  # Record the optimal split point

    return M, S


def print_optimal_parens(S, i, j):
    """
    Print the optimal parenthesization order.
    :param S: Split point matrix
    :param i: Starting matrix index
    :param j: Ending matrix index
    """
    if i == j:
        print(f"A{i + 1}", end="")  # Matrix numbers start from 1
    else:
        print("(", end="")
        print_optimal_parens(S, i, S[i][j])  # Left part
        print_optimal_parens(S, S[i][j] + 1, j)  # Right part
        print(")", end="")


# Example input
dimensions = [10, 20, 30, 40, 30]  # Matrix dimensions, corresponds to 4 matrices

# Compute the minimum cost and split points
M, S = matrix_chain_order(dimensions)

# Output the minimum cost
print("Minimum multiplication cost:", M[0][len(dimensions) - 2])

# Print the optimal parenthesization order
print("Optimal parenthesization order:")
print_optimal_parens(S, 0, len(dimensions) - 2)
