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
    def jump_search(self, nums: [int]) -> int:
        """ TLE """
        self.nums = nums
        self.min_jumps = float("inf")
        self.search(0, 0)
        print(self.min_jumps)

    def search(self, i, jumps):
        if jumps >= self.min_jumps:
            return
        if i == len(self.nums) - 1:
            self.min_jumps = min(self.min_jumps, jumps)
            return
        if i >= len(self.nums):
            return
        max_jump = self.nums[i]
        for j in range(max_jump, 0, -1):
            if i + j > len(self.nums):
                continue
            self.search(i + j, jumps + 1)

    def jump_dp_top_down(self, nums: [int]) -> int:
        """ TLE """
        self.nums = nums
        self.memo = {}
        print(self.dp_top_down(0))

    def dp_top_down(self, i) -> int:
        if i in self.memo:
            return self.memo[i]
        if i >= len(self.nums) - 1:
            return 0
        if self.nums[i] == 0:
            return float("inf")
        for j in range(self.nums[i], 0, -1):
            if i in self.memo:
                self.memo[i] = min(self.memo[i], self.dp_top_down(i + j) + 1)
            else:
                self.memo[i] = self.dp_top_down(i + j) + 1
        return self.memo[i]

    def jump_greedy(self, nums: [int]) -> int:
        if len(nums) < 2:
            return 0
        global_max_range = 0    # 全局能走到的最大距离
        local_max_range = 0     # 当前能走到的最大距离
        jumps = 0
        for i in range(len(nums) - 1):
            local_max_range = max(local_max_range, i + nums[i])
            if i == global_max_range:
                jumps += 1
                global_max_range = local_max_range
        print(global_max_range)
        return jumps

    # def jump_bfs(self, nums: [int]) -> int:
    #     if len(nums) < 2:
    #         return 0
    #     jumps = 0
    #     max_range = 0
    #     curr_max_range = 0
    #     while True:
    #         jumps += 1
    #         curr_max_range = max(max_range, i + nums[i])
    #         for r in range(curr_max_range, 0, -1):
    #             if r + nums[r] >= len(nums):
    #                 return jumps
                



Solution().jump_bfs([2, 3, 1, 1, 4])
