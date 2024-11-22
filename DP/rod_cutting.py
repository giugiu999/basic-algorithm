# P --> index: length; value: price
#j -> length
# i-> cutting length
def rod_cutting(p,n):
    dp = [0]*(n+1)
    cuts=[0]*(n+1)
    for j in range(1,n+1):
        maxvalue = float('-inf')
        for i in range(1,j+1):
            if maxvalue < p[i] + dp[j-i]:
                maxvalue = p[i] + dp[j-i]
                cuts[j]=i
        dp[j] = maxvalue
    return dp[n],cuts
def records(cuts,n):
    result = []
    while n > 0:
        result.append(cuts[n])
        n -= cuts[n]
    return result

# testing
prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30] # from 1 to 10
n = 8
max_profit,cuts = rod_cutting(prices, n)
solution = records(cuts,n)
print(f"maxvalue: {max_profit}, schema: {solution}")