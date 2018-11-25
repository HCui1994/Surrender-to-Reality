"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""

class Solution:
    def unique_path_dp(self, m, n):
        """
        dynamic programming
        注意：robot 只能向下或向右走
        """
        if not m or not n:
            return 0
        if m == 1 or n == 1:
            return 1
        # memo[i][j] 代表 从 grid[0][0] 到 grid[i][j] 有几种走法
        memo = [[1 for _ in range(n)] for _ in range(m)]
        memo[0][0] = 0
        for i in range(1, m, +1):
            for j in range(1, n, +1):
                come_from_top = memo[i - 1][j]
                come_from_left = memo[i][j - 1]
                memo[i][j] = come_from_left + come_from_top
        return memo[-1][-1]

    def test(self):
        m = 7
        n = 3
        ans = self.unique_path_dp(m, n)
        print(ans)

soln = Solution()
soln.test()