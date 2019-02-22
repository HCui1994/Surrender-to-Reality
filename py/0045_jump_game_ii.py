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
    def jump(self, nums):
        if len(nums) <= 1:
            return 0
        self.final = len(nums) - 1
        self.nums = nums
        self.memo = {}
        return self.jumper(0)

    def jumper(self, pos):
        if pos == self.final:
            return 0
        if pos > self.final:
            return float("inf")
        if self.nums[pos] == 0:
            self.memo[pos] = float("inf")
        if pos in self.memo:
            return self.memo[pos]
        self.memo[pos] = float("inf")
        for step in range(1, self.nums[pos] + 1):
            self.memo[pos] = min(self.memo[pos], self.jumper(pos + step))
        self.memo[pos] += 1
        return self.memo[pos]

    def test(self):
        nums = [2, 3, 1, 1, 4]
        print(self.jump(nums)) 


Solution().test()

