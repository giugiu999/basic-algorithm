def rod_cutting_top_down(prices, n):
    # 初始化备忘录，-1 表示尚未计算
    memo = [-1] * (n + 1)
    
    # 定义递归函数
    def memoized_cut_rod(n):
        # 如果备忘录中已经有结果，直接返回
        if memo[n] != -1:
            return memo[n]
        # 基础情况：长度为 0，收益为 0
        if n == 0:
            return 0
        # 初始化最大收益为负无穷
        max_profit = float('-inf')
        # 遍历所有切割位置
        for i in range(1, n + 1):
            # 尝试切割长度 i，计算剩余长度的最大收益
            max_profit = max(max_profit, prices[i] + memoized_cut_rod(n - i))
        # 将结果存入备忘录
        memo[n] = max_profit
        return max_profit

    # 开始递归计算
    return memoized_cut_rod(n)

# 测试数据
prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]  # 长度 0 到 10 的价格表
n = 8  # 钢条总长度

# 调用函数
max_profit = rod_cutting_top_down(prices, n)
print(f"最大收益为: {max_profit}")
