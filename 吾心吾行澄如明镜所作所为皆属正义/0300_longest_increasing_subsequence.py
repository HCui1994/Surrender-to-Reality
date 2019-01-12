"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note: 
There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n^2) complexity.
Follow up: Could you improve it to O(nlogn) time complexity?
"""


class Solution(object):
    def length_of_LIS_brutal_dp(self, nums):
        """
        a more strict forward dynamic programming solution
        """
        length = len(nums)
        dp = [1 for _ in range(length)]
        max_len_lis = 0
        for i in range(length):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            max_len_lis = max(dp[i], max_len_lis)
        print(dp)

    def test(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        self.length_of_LIS_brutal_dp(nums)


Solution().test()
