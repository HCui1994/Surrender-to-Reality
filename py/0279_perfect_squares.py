"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""
import math

class Solution:
    def num_squares_dp1(self, n):
        """
        动态规划？
        target      sum of
        1           1
        2           1 1
        3           1 1 1
        4           4
        5           4 1
        6           4 2
        7           4 2 1
        8           4 4
        9           9
        10          9 1
        11          9 1 1
        12          4 4 4  !!!
        13          9 4  !!!
        14          9 4 1  
        15          9 4 1 1
        16          16

        TLE ...
        """
        if n < 2:
            return n
        memo = [float("inf") for _ in range(n + 1)]
        memo[1] = 1
        print(memo)
        for target in range(2, n + 1, +1):
            if int(math.sqrt(target)) == math.sqrt(target):
                memo[target] = 1
                continue
            for j in range(1, target // 2 + 1, +1):
                addend1 = memo[j]
                addend2 = memo[target - j]
                memo[target] = min(memo[target], addend1 + addend2)
        return memo[-1]

    def num_squares_dp2(self, n):
        """
        改进型
        仍然 TLE
        """
        if n < 2:
            return n
        memo = [float("inf") for _ in range(n + 1)]
        memo[0], memo[1] = 0, 1
        for target in range(2, n + 1, +1):
            # 每个 target 都可以看作是一个完全平方数 A 和另外一个数 B 的和
            # 此 B 即是子问题
            for sqrt1 in range(1, int(math.sqrt(target)) + 1, +1):
                a = sqrt1 ** 2
                b = target - a
                memo[target] = min(memo[target], memo[b] + 1)
        # print(memo)
        return memo[-1]

    _dp = [0]
    def num_squares_static_dp(self, n):
        dp = self._dp
        while len(dp) <= n: # for target in range(2, n + 1, +1):
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]
    

    def test(self):
        n = 13
        print(self.num_squares_dp2(n))


Solution().test()