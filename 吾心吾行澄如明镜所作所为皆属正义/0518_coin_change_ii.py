"""
You are given coins of different denominations and a total amount of money. 
Write a function to compute the number of combinations that make up that amount. 
You may assume that you have infinite number of each kind of coin.

Example 1:
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10] 
Output: 1

Note:
You can assume that
1.  0 <= amount <= 5000
2.  1 <= coin <= 5000
3.  the number of coins is less than 500
4.  the answer is guaranteed to fit into signed 32-bit integer
"""


class Solution(object):

    def coin_change_dp(self, total_amount, coins):
        """
        dp[i] 代表 amount = i 时，有多少种分配方法
        """
        # import numpy as np
        dp = [0 for _ in range(total_amount + 1)]
        dp[0] = 1  # amount = 0 时，只有 1 种分配方法
        for coin_idx in range(len(coins)):
            for amount in range(total_amount + 1):
                if amount >= coins[coin_idx]:
                    collect = dp[amount - coins[coin_idx]]
                    uncollect = dp[amount]
                    dp[amount] = collect + uncollect
        print(dp)
        return dp[-1]

    # def coin_change_dfs_memoization(self, total_amoint, coins):
    #     memo = {}
    #     memo[0] = 1
    #     self.dfs(total_amoint, coins, memo)
    #     print(memo)

    # def dfs(self, amount, coins, memo):
    #     print(memo, amount)
    #     if memo.get(amount):
    #         return memo[amount]
    #     memo[amount] = 0
    #     for coin in coins:
    #         if amount >= coin:
    #             memo[amount] += self.dfs(amount - coin, coins, memo)
    #     return memo[amount]


    def test(self):
        amount = 5
        coins = [1, 2, 5]
        self.coin_change_dfs_memoization(amount, coins)


Solution().test()
