class Solution:
    def twoSum(self, nums, target):
        nums_dict = {}
        for i, num in enumerate(nums):
            nums_dict[num] = i
        for i, num in enumerate(nums):
            if target - num in nums_dict.keys() and nums_dict[target-num] != i: # 注意，一个数只能用一次
                return [i, nums_dict[target-num]]

