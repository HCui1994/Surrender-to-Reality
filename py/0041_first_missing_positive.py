"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.

0854 -> 1010 (66) ac
13.19%
"""

class Solution:
    # def first_missing_positive(self, nums):
    #     """
    #     寻找一个空洞，肯定和长度有关，能否用数值本身代替下标？
    #     如何能够标识一个正数曾经出现过？
    #     把出现过的正数，按顺序放在数列的相应位置上
    #     再遍历一遍数列，找到第一个矛盾，即为答案

    #     假设数列为 -1, -2, 5, 2, 3, 1
    #     长度 6，最大值 5，偏移量 0
        
    #     idx     arr
    #     0       -1 -2 5 2 3 3   （非正数，跳过）
    #             ^
    #     1       -1 -2 5 2 3 3   （非整数，跳过）
    #                 ^
    #     2       -1 -2 2 2 3 5   （5 放在 idx = 4 位置，互换）
    #                   ^
    #     3       -1 2 3 -2 5 3   （2 放在 idx = 1 位置，互换）
    #                     ^
    #     4       -1 2 3 -2 5 3   （5 放在 idx = 4 位置，互换）
    #                       ^
    #     5       -1 2 3 -2 5 3   （3 放在 idx = 2 位置，互换）
    #                         ^   
    #     """
    #     length = len(nums)
    #     max_num = max(nums)
    #     min_num = min(nums)
    #     offset = max_num - length - 1
    #     for idx in range(length):
    #         nums[idx] -= offset
    #     for idx in range(length):
    #         num_de_offset = nums[idx]
    #         num_origin = num_de_offset + offset
    #         if num_origin:
    #             # 如果原数不是正数，跳过
    #             continue
    #         nums[idx], nums[num_de_offset]

    def first_missing_positive(self, nums):
        """
        http://www.cnblogs.com/grandyang/p/4395963.html
        要求 O(1) 的空间复杂度，只能考虑覆盖原有数组，用数列的值代替数列下表
        """
        length = len(nums)
        for i in range(length):
            while nums[i] > 0 and nums[i] <= length and nums[nums[i] - 1] != nums[i]:
                # print(nums)
                # 注意，要一只换到不能换为止，避免在不完全的置换后跳指针进入下一轮循环，使得疏漏某些 case
                num1, num2 = nums[i], nums[nums[i] - 1]
                nums[nums[i] - 1], nums[i] = num1, num2
                # print(i, num1, num2)
                # break
        for i in range(1, length + 1):
            idx = i - 1
            if i != nums[idx]:
                return i
        return length + 1
        


    def test(self):
        nums = [-2,3,4,1,2,6,-2,3,-9,0,9]
        print(self.first_missing_positive(nums))

Solution().test()


                

        