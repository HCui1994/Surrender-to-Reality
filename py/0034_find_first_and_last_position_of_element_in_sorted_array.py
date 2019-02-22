"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""


class Solution(object):
    def search_range(self, nums, target):
        def bisect(target):
            low, high = 0, len(nums)
            while low < high:
                mid = low + (high - low) // 2
                if nums[mid] >= target:
                    high = mid
                else:
                    low = mid + 1
            return low

        first = bisect(1)
        if not (first <= len(nums) and nums[first] == target):
            return [-1, -1]
        last = bisect(2)
        print(first, last)

    def test(self):
        nums = [1, 1, 1]
        target = 1
        self.search_range(nums, target)


Solution().test()
