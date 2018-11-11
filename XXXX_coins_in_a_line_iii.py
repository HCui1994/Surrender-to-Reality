"""
There are n coins in a line. Two players take turns to take a coin from one of the ends of the line until there are no more coins left. The player with the larger amount of money wins.

Could you please decide the first player will win or lose?

Have you met this question in a real interview? Yes
Example
Given array A = [3,2,2], return true.

Given array A = [1,2,4], return true.

Given array A = [1,20,4], return false.

"""
import numpy as np
class Solution:
    def win_or_lose(self, coins):
        num_coins = len(coins)
        sum = [0 for _ in range(num_coins + 1)]
        for i in range(1, num_coins + 1):
            sum[i] = sum[i - 1] + coins[i - 1]
        memo = [[None for _ in range(num_coins)] for _ in range(num_coins)]
        for i in range(num_coins):
            memo[i][i] = coins[i]
        for l in range(2, num_coins + 1, +1):
            for i in range(num_coins):
                j = i + l - 1
                if j >= num_coins:
                    continue
                s = sum[j + 1] - sum[i]
                memo[i][j] = max(s - memo[i + 1][j], s - memo[i][j - 1])
        print(memo[0][num_coins - 1] > sum[num_coins] // 2)
        print(np.array(memo))




    def test(self):
        coins = [1, 20, 4]
        self.win_or_lose(coins)



Solution().test()