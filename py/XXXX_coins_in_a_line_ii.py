"""
There are n coins with different value in a line. Two players take turns to take one or two coins from left side until there are no more coins left. 
The player who take the coins with the most value wins.

Could you please decide the first player will win or lose?

Example
Given values array A = [1,2,2], return true.

Given A = [1,2,4], return false.
"""


class Solution:
    def win_or_lose_1(self, coins):
        """
        i：当前剩余 i 个硬币
        memo[i]: 先手玩家取得的最大硬币价值
        """
        num_coins = len(coins)
        if not num_coins:
            return False
        if num_coins <= 2:
            return True
        memo = [None for _ in range(num_coins + 1)]
        max_value = self._mem_search(coins, num_coins, memo)
        print(max_value * 2 > sum(coins))

    def _mem_search(self, coins, coins_remaining, memo):
        if memo[coins_remaining] is not None:
            return memo[coins_remaining]
        if coins_remaining == 0:
            memo[coins_remaining] = 0
        elif coins_remaining == 1:
            memo[coins_remaining] = coins[-1]
        elif coins_remaining == 2:
            memo[coins_remaining] = coins[-1] + coins[-2]
        elif coins_remaining == 3:
            memo[coins_remaining] = coins[-2] + coins[-3]
        else:
            # 让对手的选择最小化
            pick_one = min(
                self._mem_search(coins, coins_remaining - 1 - 1, memo),
                self._mem_search(coins, coins_remaining - 1 - 2,
                                 memo)) + coins[len(coins) - coins_remaining]
            pick_two = min(
                self._mem_search(coins, coins_remaining - 2 - 1, memo),
                self._mem_search(
                    coins, coins_remaining - 2 - 2,
                    memo)) + coins[len(coins) - coins_remaining] + coins[
                        len(coins) - coins_remaining + 1]
            memo[coins_remaining] = max(pick_one, pick_two)
        return memo[coins_remaining]


soln = Solution()
coins = [1,2,4]
soln.win_or_lose_1(coins)