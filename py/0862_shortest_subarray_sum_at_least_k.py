"""
Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.
If there is no non-empty subarray with sum at least K, return -1.

Example 1:
Input: A = [1], K = 1
Output: 1

Example 2:
Input: A = [1,2], K = 4
Output: -1

Example 3:
Input: A = [2,-1,2], K = 3
Output: 3
 
Note:
1.  1 <= A.length <= 50000
2.  -10 ^ 5 <= A[i] <= 10 ^ 5
3.  1 <= K <= 10 ^ 9
"""

import collections


class Solution(object):
    def shortest_subarray_sum_at_lesast_k(self, nums, k):
        """
        TLE
        """
        memo = collections.Counter()
        memo[0] = -1
        summation = 0
        length = float("inf")
        for end, num in enumerate(nums):
            summation += num
            for prev_summation, prev_end in memo.items():
                if summation - prev_summation >= k:
                    length = min(end - prev_end, length)
            memo[summation] = end
        return -1 if length == float("inf") else length

    def test(self):
        A = [2, -1, 2]
        K = 3
        print(self.shortest_subarray_sum_at_lesast_k(A, K))


Solution().test()
