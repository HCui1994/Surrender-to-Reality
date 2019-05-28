"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""

class Solution(object):
    def find_min(self, nums):
        if not nums:
            return None
        left, right = 0, len(nums)
        if right - left < 3:
            return min(nums)
        while right - left >= 3:
            mid = left + (right - left) // 2
            if nums[left] < nums[mid]:
                