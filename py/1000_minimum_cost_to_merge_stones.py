"""
There are N piles of stones arranged in a row.  The i-th pile has stones[i] stones.
A move consists of merging exactly K consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these K piles.
Find the minimum cost to merge all piles of stones into one pile.  If it is impossible, return -1.

Example 1:

Input: stones = [3,2,4,1], K = 2
Output: 20
Explanation: 
We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.

Example 2:
Input: stones = [3,2,4,1], K = 3
Output: -1
Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.

Example 3:
Input: stones = [3,5,1,2,6], K = 3
Output: 25

Explanation: 
We start with [3, 5, 1, 2, 6].
We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
We merge [3, 8, 6] for a cost of 17, and we are left with [17].
The total cost was 25, and this is the minimum possible.
 
Note:
1 <= stones.length <= 30
2 <= K <= 30
1 <= stones[i] <= 100
"""

import numpy as np

from copy import copy


class Solution(object):
    def merge_stones(self, stones, k):
        num_stones = len(stones)
        q, r = divmod((num_stones - k), (k - 1))
        if r:
            return -1
        cum_sum = [0]
        summation = 0
        for i, num in enumerate(stones):
            summation += num
            cum_sum.append(summation)
        dp = [[float("inf") for _ in range(num_stones + 1)] for _ in range(num_stones)]
        # init
        for i in range(num_stones - k + 1):
            dp[i][i + k] = sum(stones[i: i + k])
        for l in range(k + k - 1, num_stones + 1):
            for i in range(num_stones):
                j = i + l
                if j > num_stones:
                    continue
                prev_l = l - k + 1
                for p in range(i, j):
                    q = p + prev_l
                    if q > j:
                        continue
                    before = cum_sum[p] - cum_sum[i]
                    mid = dp[p][q]
                    after = cum_sum[j] - cum_sum[q]
                    dp[i][j] = min(dp[i][j], before + mid + after + mid)
        print(np.array(dp))

    def merge_stones_recur(self, stones, k):
        num_stones = len(stones)
        q, r = divmod((num_stones - k), (k - 1))
        if r:
            return -1
        self.memo = {}
        self.k = k
        self.stones = stones
        return self.recur(stones, r + 1)

    def recur(self, stones, flag):
        # print(stones)
        if len(stones) == 1:
            return 0
        stones = copy(stones)
        self.memo[flag] = float("inf")
        for i in range(len(stones) - self.k + 1):
            summation = sum(stones[i: i + self.k])
            self.memo[flag] = min(self.memo[flag], self.recur(stones[:i] + [summation] + stones[i + self.k:], flag - 1) + summation)
        return self.memo[flag]


soln = Solution()
print(soln.merge_stones(stones=[3, 2, 4, 1], k=2))
