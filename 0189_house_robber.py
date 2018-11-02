# dynamic programming EASY

class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        """
        用二维数组存储子问题解
        dp[i][0], 不抢劫商店i；dp[i][1]抢劫商店i
        """
        dp = [[0, 0] for _ in range(len(nums)+1)]
        # 初始化
        dp[1][0] = 0
        dp[1][1] = nums[0]
        for i in range(2, len(dp), +1):
            """不抢商店i，可以抢i-1，也可以不抢i-1"""
            dp[i][0] = max(dp[i-1][1], dp[i-1][0])
            """抢了商店i，一定没有抢i-1"""
            dp[i][1] = dp[i-1][0] + nums[i-1]
        return max(dp[-1])

nums = [2,1,1,2]
soln = Solution()
print(soln.rob(nums))