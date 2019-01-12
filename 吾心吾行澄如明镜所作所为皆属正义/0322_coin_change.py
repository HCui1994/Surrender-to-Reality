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


class Solution(object):

    def coin_change_dp_primitive(self, coins, total_amount):
        """
        转化为 0-1 背包
        """
        import numpy as np
        coins_list = []
        for coin in coins:
            coins_list += [coin] * (total_amount // coin)
        dp = np.ones(shape=(len(coins_list) + 1, total_amount + 1)) * float("inf")
        for coin_idx in range(len(coins_list) + 1):
            dp[coin_idx][0] = 0
        for coin_idx in range(len(coins_list)):
            dp_coin_idx = coin_idx + 1
            for amount in range(total_amount + 1):
                collect = dp[dp_coin_idx - 1][amount - coins_list[coin_idx]] + 1
                uncollct = dp[dp_coin_idx - 1][amount]
                # print("list: {}\tamount: {}\tcoin: {}\tcollect: {}\tuncollect: {}".format(coins_list[:coin_idx + 1], amount, coins_list[coin_idx], collect, uncollct))
                dp[dp_coin_idx][amount] = min(collect, uncollct)
        print(dp)
        return -1 if dp[-1][-1] == float("inf") else dp[-1][-1]

    def coin_change_dp_primitive_mem_opt(self, coins, total_amount):
        import numpy as np
        coins.sort()
        coin_dict = {}
        for coin in coins:
            tmp = coin
            while tmp <= total_amount:
                coin_dict[tmp] = tmp // coin
                tmp *=2
        coin_list = sorted(coin_dict.keys())
        dp = np.ones(shape=(len(coin_list) + 1, total_amount + 1)) * float("inf")
        for coin_idx in range(len(coin_list) + 1):
            dp[coin_idx][0] = 0
        for coin_idx in range(len(coin_list)):
            dp_coin_idx = coin_idx + 1
            for amount in range(total_amount + 1):
                print(amount - coin_list[coin_idx], dp[dp_coin_idx - 1][amount - coin_list[coin_idx]])
                # if amount >= coin_list[coin_idx]:
                collect = dp[dp_coin_idx - 1][amount - coin_list[coin_idx]] + coin_dict[coin_list[coin_idx]]
                uncollect = dp[dp_coin_idx - 1][amount]
                dp[dp_coin_idx][amount] = min(collect, uncollect)
        print(dp)
        return -1 if dp[-1][-1] == float("inf") else dp[-1][-1]

    def coin_change_dp_better_mem_opt(self, coins, total_amount):
        """
        动态规划：dp[i] 表示达到 amount = i 最少需要多少个硬币
        """
        dp = [float("inf") for _ in range(total_amount + 1)]
        # amount = 0 时需要 0 个硬币
        dp[0] = 0
        for amount in range(1, total_amount + 1):
            for coin in coins:
                if amount >= coin:
                    collect = dp[amount - coin] + 1
                    uncollect = dp[amount]
                    dp[amount] = min(collect, uncollect)
        print(dp)
        return -1 if dp[-1] == float("inf") else dp[-1]

    def coin_change_dfs_memoization(self, coins, total_amount):
        """
        TLE ???!!!
        与 dp 是完全相同的方法，为何会 tle 。。。 
        """
        if total_amount < 1:
            return 0
        coins = set(coins)
        memo = {amount : float("inf") for amount in range(total_amount + 1)}
        memo[0] = 0
        for coin in coins:
            memo[coin] = 1
        self.dfs(coins, total_amount, memo)
        print(memo)
        return -1 if memo[total_amount] == float("int") else memo[total_amount]

    def dfs(self, coins, amount, memo):
        if memo[amount] and memo[amount] != float("inf"):
            return memo[amount]
        for coin in coins:
            if amount >= coin:
                memo[amount] = min(memo[amount], self.dfs(coins, amount - coin, memo))
        memo[amount] += 1
        return memo[amount]

    def test(self):
        coins = [1, 2, 5]
        amount = 11
        # self.coin_change_dp_primitive(coins, amount)
        # self.coin_change_dp_primitive_mem_opt(coins, amount)
        # self.coin_change_dp_better_mem_opt(coins, amount)
        self.coin_change_dfs_memoization(coins, amount)


Solution().test()
