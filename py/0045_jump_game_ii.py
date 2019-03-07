"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:
Input: [2,3,1,1,4]
Output: 2

Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""


class Solution(object):
    def jump_greedy(self, nums):
        reachable = nums[0]
        

    def test(self):
        nums = [2, 3, 1, 1, 4]
        print(self.jump(nums)) 


Solution().test()

