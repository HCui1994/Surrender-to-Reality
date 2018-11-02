"""Previouely House Robber I: 0189"""
"""循环数组，错一位，求两个解"""
class Solution:
    def rob(self, nums):
        def rob_space_opt(nums):
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]

            """商店i处的收益仅和i-1的收益相关"""
            """只需要存i-1"""
            dp = [0, nums[0]]
            for i in range(1, len(nums), +1):
                rob_current = dp[0] + nums[i]
                not_rob_current = max(dp[0], dp[1])
                dp = [not_rob_current, rob_current]
            return max(rob_current, not_rob_current)
        if not nums:
            return 0
        if len(nums) <= 3:
            return max(nums)

        return max(rob_space_opt(nums[:-1]), rob_space_opt(nums[1:]))

soln = Solution()
nums = [1,2,3,1]
print(soln.rob(nums))