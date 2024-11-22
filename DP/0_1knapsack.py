# dp[i][j] ->i:item; j;capacity
def knapsack(weight,value,W):
    # create the table
    dp =[]
    num = len(weight)
    for i in range(num+1):
        row = []
        for j in range(W+1):
            row.append(0)
        dp.append(row) # equals to dp = [[0] * (W+1) for _ in range(num+1)]

    for i in range(1, num + 1):
        for d in range(W + 1):
            if weight[i - 1] <= d:  # selected
                dp[i][d] = max(dp[i - 1][d], dp[i - 1][d - weight[i - 1]] + value[i - 1])
            else:
                dp[i][d] = dp[i - 1][d] # not selected
    
    # track selected items
    selected_items = []
    d = W
    for i in range(num, 0, -1):  
        if dp[i][d] != dp[i - 1][d]:
            selected_items.append(i - 1)
            d -= weight[i - 1] 

    selected_items.reverse() # original order
    return dp[num][W], selected_items

# testing
weights = [2, 3, 4]
values = [3, 4, 5]
W = 5

max_value, selected_items = knapsack(weights, values, W)

print(f"Maximum value in knapsack: {max_value}")
print("Selected items (0-based index):")
for item in selected_items:
    print(f"  Item {item + 1} (weight: {weights[item]}, value: {values[item]})")