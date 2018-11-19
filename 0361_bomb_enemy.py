"""
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note: You can only put the bomb at an empty cell.

Example:
Input: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
Output: 3 
Explanation: For the given grid,

0 E 0 0 
E 0 W E 
0 E 0 0

Placing a bomb at (1,1) kills 3 enemies.
"""

class Solution:

    def bomb_enemy_dp(self, grid):
        if not grid:
            return 0
        if not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        memo_top_left = [[[0, 0] for _ in range(n + 1)] for _ in range(m + 1)]
        memo_bottom_right = [[[0, 0] for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            mi = i + 1
            for j in range(n):
                mj = j + 1
                if grid[i][j] == "W":
                    memo_top_left[mi][mj] = [0, 0]
                elif grid[i][j] == "E":
                    memo_top_left[mi][mj] = [memo_top_left[mi][mj - 1][0] + 1, memo_top_left[mi - 1][mj][1] + 1]
                else:
                    memo_top_left[mi][mj] = [memo_top_left[mi][mj - 1][0], memo_top_left[mi - 1][mj][1]]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mi, mj = i, j
                if grid[i][j] == "W":
                    memo_bottom_right[mi][mj] = [0, 0]
                elif grid[i][j] == "E":
                    memo_bottom_right[mi][mj] = [memo_bottom_right[mi][mj + 1][0] + 1, memo_bottom_right[mi + 1][mj][1] + 1]
                else:
                    memo_bottom_right[mi][mj] = [memo_bottom_right[mi][mj + 1][0], memo_bottom_right[mi + 1][mj][1]]
        max_enemy = 0
        for i in range(m):
            mi = i + 1
            for j in range(n):
                mj = j + 1
                if grid[i][j] == "0":
                    max_enemy = max(max_enemy, sum(memo_top_left[mi][mj]) + sum(memo_bottom_right[i][j]))
        return max_enemy

    def test(self):
        grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
        ans = self.bomb_enemy_dp(grid)
        print(ans)


soln = Solution()
soln.test()