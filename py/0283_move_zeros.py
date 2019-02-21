"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
1.  You must do this in-place without making a copy of the array.
2.  Minimize the total number of operations.


SCORE:
2000 -> 2009 (9)
0 attempt AC
87.54%
"""

class Solution(object):
    def move_zeros(self, nums):
        movement = 0
        idx = 0
        while idx < len(nums):
            print(idx)
            if nums[idx] == 0:
                movement += 1
            else:
                nums[idx - movement], nums[idx] = nums[idx], 0
            idx += 1
        for idx in range(movement):
            nums[len(nums) - idx - 1] = 0

    def test(self):
        nums = []
        self.move_zeros(nums)
        print(nums)


Solution().test()
            
        