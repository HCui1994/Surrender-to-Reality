"""
Given n balloons, indexed from 0 to n-1. 
Each balloon is painted with a number on it represented by array nums. 
You are asked to burst all the balloons. 
If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. 
Here left and right are adjacent indices of i. 
After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:
Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""
import numpy as np

class Solution(object):
    def max_coins(self, nums):
        """
        动态规划：dp[i][j] 表示打爆 nums[i .. j]，按照某种顺序能够获取的最大得分
        初始化：仅有一个气球 
        """
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0 for _ in range(n)] for _ in range(n)]
        # 初始化
        for i in range(n):
            ni = i + 1
            dp[i][i] = nums[ni - 1] * nums[ni] * nums[ni + 1]
        # 状态转移
        for l in range(n):
            for i in range(n - 1):
                j = i + l
                if j >= n:
                    continue
                ni, nj = i + 1, j + 1
                for k in range(i, j + 1):
                    nk = k + 1
                    if k == i:
                        dp[i][j] = max(dp[i + 1][j] + nums[ni - 1] * nums[nk] * nums[nj + 1], dp[i][j])
                    elif k == j:
                        dp[i][j] = max(dp[i][j - 1] + nums[ni - 1] * nums[nk] * nums[nj + 1], dp[i][j])
                    else:
                        dp[i][j] = max(dp[i][k - 1] + dp[k + 1][j] + nums[ni - 1] * nums[nk] * nums[nj + 1], dp[i][j])
        print(np.array(dp))
        return dp[0][n - 1]






    def test(self):
        nums = [3]
        print(self.max_coins(nums))

Solution().test()
