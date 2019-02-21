"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""

import time

class Solution(object):
    def sort_colors(self, nums):
        """
        LC0283 move zeros
        """
        if not nums:
            return nums
        zero_ptr, two_ptr = 0, len(nums) - 1
        ptr = 0
        while ptr < two_ptr:
            if nums[ptr] == 2:
                while two_ptr > 0 and nums[two_ptr] == 2:
                    two_ptr -= 1
                nums[ptr], nums[two_ptr] = nums[two_ptr], nums[ptr]
            ptr += 1
        while ptr > zero_ptr:
            if nums[ptr] == 0:
                while zero_ptr < two_ptr and nums[zero_ptr] == 0:
                    zero_ptr += 1
                nums[ptr], nums[zero_ptr] = nums[zero_ptr], nums[ptr]
            ptr -= 1
        print(nums)

        

    def test(self):
        nums = [0, 0, 0]
        self.sort_colors(nums)


Solution().test()