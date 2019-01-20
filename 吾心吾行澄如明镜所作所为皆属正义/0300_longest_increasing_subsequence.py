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

        dp[i] 表示 nums[0 .. i] 中 LIS 的长度

        类似于双指针思路：
        1.  ptr1 确定一段数列的末尾
        2.  遍历 ptr2 from 0 to ptr1-1
        3.  如果 nums[ptr2] < nums[ptr1]，...
        """
        length = len(nums)
        dp = [1 for _ in range(length)] # 初始化，所有位置上的 LIS 长度至少为 1
        max_len_lis = 0
        for i in range(length):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                print(dp, nums, i, j)
            max_len_lis = max(dp[i], max_len_lis)
        print(dp)

    def length_of_LIS_trivial(self, nums):
        """
        先将数列排序，再求排序数列与原数列的 LCS
        """
        import numpy as np
        length = len(nums)
        sorted_nums = sorted(nums)
        dp = [[0 for _ in range(length + 1)] for _ in range(length + 1)]
        # print(np.array(dp))
        for i in range(length):
            dpi = i + 1
            for j in range(length):
                dpj = j + 1
                if nums[i] == sorted_nums[j]:
                    dp[dpi][dpj] = dp[dpi - 1][dpj - 1] + 1
                else:
                    dp[dpi][dpj] = max(dp[dpi - 1][dpj], dp[dpi][dpj - 1])
        return dp[-1][-1] if nums else 0

    def test(self):
        nums = [1,3,2,5,4]
        print(self.length_of_LIS_trivial(nums))


Solution().test()
