"""
You are given coins of different denominations and a total amount of money amount. 
Write a function to compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Note:
You may assume that you have an infinite number of each kind of coin.
"""

import numpy as np

class Solution(object):
    def coin_change(self, coins, amount):
        """
        背包问题？
        如何装能够将背包刚好装满，且是用最少的物品数量
        MLE
        """
        # 转换为 0-1 背包问题
        dp = np.ones((amount + 1, )) * float("inf")
        dp[0] = 0
        print(dp)
        for amt in range(1, amount + 1):
            for coin_idx in range(len(coins)):
                if coins[coin_idx] <= amt:
                    dp[amt] = min(dp[amt], dp[amt - coins[coin_idx]] + 1)
        return -1 if dp[amount] > amount else dp[amount]

    def test(self):
        coins = [1, 2, 5]
        amount = 11
        print(self.coin_change(coins, amount))


Solution().test()
        