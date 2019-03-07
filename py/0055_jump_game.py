"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""


class Solution(object):
    def can_jump_recur_memo(self, nums):
        """
        实际 brutal
        TLE, O(n^2)
        """
        if len(nums) <= 1:
            return True
        self.nums = nums
        self.memo = {}
        min_step = self.jump(0)
        return min_step != float("inf")

    def jump(self, idx):
        if idx == len(self.nums) - 1:
            return 0
        if idx >= len(self.nums):
            return float("inf")
        if self.nums[idx] == 0:
            return float("inf")
        if idx in self.memo:
            return self.memo[idx]
        self.memo[idx] = float("inf")
        max_step = self.nums[idx]
        for step in range(max_step, 0, -1):
            self.memo[idx] = min(self.memo[idx], self.jump(idx + step))
        self.memo[idx] += 1
        return self.memo[idx]

    # def can_jump_bit(self, nums):
    #     """
    #     树状数组中的染色问题。
    #     我们可以把jump的过程看成是染色，还是从左到右枚举位置
    #     比如枚举到 index=0 位置时，nums[0]=5，也就是说从 index=0 的位置一直可以走到 index=5 的位置, 那么我们可以把1~5这一段进行染色
    #     当枚举到 index=1 时，如何判断能不能走到这一步呢？
    #     只需求该点被染色的次数，如果大于0，那么就是能到达，然后从该点向后继续染色，最后判断最后一点有没有被染色即可。复杂度 O(nlongn)。
    #     """
    #     fenwick = [0] * (len(nums) + 1)
    #     nums = nums[::-1]

    #     def lowbit(x):
    #         return x & -x

    #     def udpate(index, val):
    #         while index < len(fenwick):
    #             fenwick[index] += val
    #             index += lowbit(index)

    #     def query(index):
    #         res = 0
    #         while index > 0:
    #             res += fenwick[index]
    #             index -= lowbit(index)
    #         return res

    def can_jump_greedy(self, nums):
        reachable = 0  # 能够到达的最远的距离
        for pos, step in enumerate(nums):
            if pos > reachable:  # 当前index小于能达到的最远距离，说明当前index无法达到
                continue
            reachable_from_curr_pos = pos + step
            reachable = max(reachable, reachable_from_curr_pos)
            if reachable >= len(nums) - 1:
                return True
        return False

    def test(self):
        nums = [2, 3, 1, 1, 4]
        print(self.can_jump_greedy(nums))
        nums = [3, 2, 1, 0, 4]
        print(self.can_jump_greedy(nums))


Solution().test()
