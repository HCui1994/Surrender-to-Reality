"""
This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes N-1 hops.  
Each hop must be from one key to another numbered key.

Each time it lands on a key (including the initial placement of the knight), it presses the number of that key, pressing N digits total.

How many distinct numbers can you dial in this manner?

Since the answer may be large, output the answer modulo 10^9 + 7.


Example 1:

Input: 1
Output: 10
Example 2:

Input: 2
Output: 20
Example 3:

Input: 3
Output: 46
 
Note:
1 <= N <= 5000
"""
import numpy as np


class Solution(object):
    def knight_dialer(self, n):
        self.memo = {}
        self.move = {1: [6, 8],
                     2: [7, 9],
                     3: [4, 8],
                     4: [3, 9, 0],
                     5: [],
                     6: [1, 7, 0],
                     7: [1, 6],
                     8: [1, 3],
                     9: [4, 3],
                     0: [4, 6]}
        nnums = 0
        for digit in range(10):
            nnums += self.dialer(digit, n) % 1000000007
        return nnums % 1000000007

    def dialer(self, digit, n):
        if (digit, n) in self.memo:
            return self.memo[digit, n]
        if n == 0:
            return 1
        nnums = 0
        for next_digit in self.move[digit]:
            nnums += self.dialer(next_digit, n - 1) % 1000000007
        self.memo[digit, n] = nnums % 1000000007
        return self.memo[digit, n]

    def knight_dialer_dp(self, n):
        move = {1: [6, 8],
                2: [7, 9],
                3: [4, 8],
                4: [3, 9, 0],
                5: [],
                6: [1, 7, 0],
                7: [2, 6],
                8: [1, 3],
                9: [4, 2],
                0: [4, 6]}
        dp = [[0 for _ in range(10)] for _ in range(n)]
        dp[0] = [1] * 10  # 初始化，只有一个数字时，只有一种跳法
        for jump in range(1, n):
            for curr_digit in range(10):
                for prev_digit in move[curr_digit]:
                    dp[jump][curr_digit] += dp[jump - 1][prev_digit]
                    dp[jump][curr_digit] %= 1000000007
        print(sum(dp[-1]))
        return sum(dp[-1])

    def test(self):
        self.knight_dialer_dp(5)


Solution().test()
