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

    def rob_space_opt(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        """商店i处的收益仅和i-1的收益相关"""
        """只需要存储i，i-1"""
        dp = [[0,       0], 
              [0, nums[0]]
        ]
        for i in range(1, len(nums), +1):
            rob_current = dp[0][0] + nums[i]
            not_rob_current = max(dp[0][1], dp[1][1])
            dp = [[dp[1][0], dp[1][1]], [not_rob_current, rob_current]]
        return max(rob_current, not_rob_current)

        

nums = [2,1,1,2]
soln = Solution()
print(soln.rob_space_opt(nums))