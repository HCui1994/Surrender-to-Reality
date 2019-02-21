"""
Given a non-empty array containing only positive integers, 
    find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""


class Solution(object):
    def can_partition_dp_cum_sum(self, nums):
        """
        找到一些数字 sum 为整体 sum 的一半

        wa，错误的思路
        """
        target = sum(nums)
        if target & 1:
            return False
        target //= 2
        nums.sort()
        cum_sum_set = set()
        cum_sum = 0
        for num in nums:
            cum_sum += num
            cum_sum_set.add(cum_sum)
            if cum_sum - target in cum_sum_set:
                return True
        return False

    def can_partition_dp_backpack(self, nums):
        """
        看作背包问题，能否装满容量 sum(nums) // 2 的背包
        """
        import numpy as np
        target = sum(nums)
        if target & 1:
            return False
        dp = [[-float("inf") for _ in range(target // 2 + 1)] for _ in range(len(nums) + 1)]
        # init
        dp[0][0] = 0  # 没有物品，背包容量为 0 一定能装满
        for num_idx in range(len(nums)):
            dp[num_idx + 1][0] = 0  # 背包容量为 0，必定能装满
        for num_idx in range(len(nums)):
            dp_num_idx = num_idx + 1
            for vol in range(nums[num_idx], target // 2 + 1):
                collect = dp[dp_num_idx - 1][vol - nums[num_idx]] + nums[num_idx]
                uncollect = dp[dp_num_idx - 1][vol]
                dp[dp_num_idx][vol] = max(collect, uncollect)
        print(np.array(dp))
        return False if dp[-1][-1] == -float("inf") else True

    def test(self):
        nums = [1, 5, 5, 11]
        print(self.can_partition_dp_backpack(nums))


Solution().test()
