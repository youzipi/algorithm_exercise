"""
encoding=utf-8
_author = youzipi
date = 2019/1/13
"""
"""
index = 322

零钱兑换

给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
说明:
你可以认为每种硬币的数量是无限的。
"""

"""
dp[i]
兑换 金额 i 所需的最少硬币数

dp[i] = sum(dp[i-coins[0]], dp[i-coins[1],...)

"""


class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        _max = amount + 1
        # 默认值 不能用 -1，得用 最大值+1
        r = [_max for i in range(amount + 1)]
        r[0] = 0

        for i in range(1, amount + 1):
            min_length = _max
            for c in coins:
                if (c <= i) and (i - c) >= 0:
                    min_length = min(min_length, r[i - c] + 1)
            r[i] = min_length
        # print(r)
        return r[amount] == _max and -1 or r[amount]


if __name__ == '__main__':
    s = Solution()
    # r = s.coinChange(coins=[1, 2, 5], amount=11)
    r = s.coinChange(coins=[2, 6, 7], amount=30)
    r = s.coinChange(coins=[493, 416, 144, 164, 314, 25], amount=5607)
    print(r)
