"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

"""

""" Attention! You Can Only Move Down Or Right!! """
class Solution:
    # def minPathSum(self, grid):
    #     if not grid:
    #         return 0
    #     m, n = len(grid), len(grid[0])
    #     memo = [[None for _ in range(n)] for _ in range(m)]
    #     flag = [[False for _ in range(n)] for _ in range(m)]
        
    #     print(self._dfs(grid, memo, flag, 0, 0))
    #     print(memo)

    # def _dfs(self, grid, memo, flag, i, j):
    #     print(i, j)
    #     flag[i][j] = True
    #     if i == len(grid) - 1 and j == len(grid[0]) - 1:
    #         memo[i][j] = grid[i][j]
    #         return memo[i][j]
    #     di = [1, -1, 0, 0]
    #     dj = [0, 0, 1, -1]
    #     path_length = [float("inf") for _ in range(4)]
    #     for idx in range(4):
    #         ii = i + di[idx]
    #         jj = j + dj[idx]
    #         if ii >=0 and jj >=0 and ii < len(grid) and jj < len(grid[0]) and not flag[ii][jj]:
    #             path_length[idx] = self._dfs(grid, memo, flag, ii, jj)
    #     memo[i][j] = min(path_length) + grid[i][j]
    #     return memo[i][j]

    def minPathSum(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        memo = [[float("inf") for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    memo[i][j] = grid[i][j]
                else:
                    go_right = grid[i][j] + memo[i][j + 1]
                    go_down = grid[i][j] + memo[i + 1][j]
                    memo[i][j] = min(go_right, go_down)
        print(memo)
        return memo[0][0]



soln = Solution()
grid = [[1,2],[5,6],[1,1]]
soln.minPathSum(grid)