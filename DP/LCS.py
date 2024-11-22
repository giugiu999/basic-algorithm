# largest common subsequences
def lcs(x, y):
    n = len(x) 
    m = len(y)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i - 1] == y[j - 1]:  # equals
                dp[i][j] = dp[i - 1][j - 1] + 1
            else: 
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_result = []
    i, j = n, m
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            lcs_result.append(x[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1 # skip x[i]
        else:  
            j -= 1 # skip j[i]

    return dp[n][m], ''.join(reversed(lcs_result))

# testing
x = "CAN"
y = "AB"
lcs_length, lcs_string = lcs(x, y)
print(f"length: {lcs_length}")
print(f"LCS: {lcs_string}")