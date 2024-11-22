# O(n)
def fibonacci(n):
    dp = [0] * (n + 1) # table
    dp[0] = 0  
    dp[1] = 1 
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# testing
n = 8
result = fibonacci(n)
print(f"fibonacci({n}) = {result}")