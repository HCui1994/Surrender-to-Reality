"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:
Input: [3,0,1]
Output: 2

Example 2:
Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""

class Solution:
    def missing_number(self, nums):
        """
        要求 O(1) 的空间复杂度，只能考虑覆盖原有数组，用数列的值代替数列下表
        参考 0041 first missing positive
        """
        length = len(nums)
        for idx in range(length):
            # 全部 + 1 避免出现 0 * -1 = 0，无法反转
            nums[idx] += 1
        for idx in range(length):
            if abs(nums[idx]) - 1 < length:
                # 由于 进行了 +1 预处理，计算下标的时候需要 -1
                nums[abs(nums[idx]) - 1] *= -1
        # print(nums)
        for idx in range(length):
            if nums[idx] > 0:
                return idx
        return length

    def test(self):
        nums = [0,1,2,3,4]
        print(self.missing_number(nums))

Solution().test()