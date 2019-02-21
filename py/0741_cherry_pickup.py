"""
In a N x N grid representing a field of cherries, each cell is one of three possible integers.

0 means the cell is empty, so you can pass through;
1 means the cell contains a cherry, that you can pick up and pass through;
-1 means the cell contains a thorn that blocks your way.

Your task is to collect maximum number of cherries possible by following the rules below:

Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells (cells with value 0 or 1);
After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.
 
Example 1:
Input: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
Output: 5

Explanation: 
The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.
"""
import numpy as np
import time


class Solution(object):
    def cherry_pickup_dfs(self, grid):
        """
        暴力搜索！！！
        TLE
        """
        if not grid or not grid[0]:
            return 0
        self.grid = grid
        self.m, self.n = len(grid), len(grid[0])
        self.max_cherry = 0
        self.walker(0, 0, 0)
        return self.max_cherry

    def walker(self, i, j, cherry, is_ret=False):
        # print(i, j)
        # print(self.m, self.n)
        if not is_ret:  # 去程
            if i == self.m - 1 and j == self.n - 1:  # 到达去程终点
                if self.grid[i][j] == 1:
                    cherry += 1
                elif self.grid[i][j] == -1:
                    return  # 死路
                backup = self.grid[i][j]
                self.grid[i][j] = 0
                is_ret = True  # 开始返程
                self.walker(i, j, cherry, is_ret)
                self.grid[i][j] = backup
            else:
                if self.grid[i][j] == 1:
                    cherry += 1
                elif self.grid[i][j] == -1:
                    return  # 死路
                backup = self.grid[i][j]
                self.grid[i][j] = 0
                di, dj = [0, 1], [1, 0]
                for idx in range(2):
                    ii, jj = i + di[idx], j + dj[idx]
                    if ii < self.m and jj < self.n:  # 可行的走法
                        self.walker(ii, jj, cherry, is_ret)
                self.grid[i][j] = backup
        else:  # 返程
            if i == 0 and j == 0:  # 回到起点，更新最佳纪录
                self.max_cherry = max(self.max_cherry, cherry)
                return
            else:
                if self.grid[i][j] == 1:
                    cherry += 1
                elif self.grid[i][j] == -1:
                    return  # 死路
                backup = self.grid[i][j]
                self.grid[i][j] = 0
                di, dj = [0, -1], [-1, 0]
                for idx in range(2):
                    ii, jj = i + di[idx], j + dj[idx]
                    if ii >= 0 and jj >= 0:
                        self.walker(ii, jj, cherry, is_ret)
                self.grid[i][j] = backup

    def cherry_pickup_recursion_with_memoization(self, grid):
        """
        wa ???
        """
        import copy
        if not grid or not grid[0]:
            return 0
        self.grid, self.m, self.n = grid, len(grid), len(grid[0])
        self.memo = {}
        round_valid, round_cherry = self.walker_memoization(0, 0, False)
        return round_cherry if round_valid else 0

    def walker_memoization(self, i, j, is_ret):
        if i < 0 or j < 0 or i >= self.m or j >= self.n:  # ivalid index
            return False, 0     # invalid path, 0 cherries
        if self.grid[i][j] == -1:  # dead end
            return False, 0   # invalid path, 0 cherries
        print(i, j)
        print(np.array(self.grid))
        print(self.memo)
        time.sleep(5)
        if (i, j, is_ret) in self.memo:
            return self.memo[i, j, is_ret]
        if not is_ret:  # 去程
            if i == self.m - 1 and j == self.n - 1:  # reach bottom right corner
                is_cherry = self.grid[i][j]
                self.grid[i][j] = 0
                ret_valid, ret_cherry = self.walker_memoization(i, j, True)
                return ret_valid, ret_cherry + is_cherry
            else:
                is_cherry = self.grid[i][j]  # backup status
                self.grid[i][j] = 0
                right_valid, right_cherry = self.walker_memoization(i, j + 1, False)
                down_valid, down_cherry = self.walker_memoization(i + 1, j, False)
                if not right_valid and not down_valid:
                    self.memo[i, j, is_ret] = False, 0
                elif right_valid and not down_valid:
                    self.memo[i, j, is_ret] = True, right_cherry + is_cherry
                elif not right_valid and down_valid:
                    self.memo[i, j, is_ret] = True, down_cherry + is_cherry
                else:
                    self.memo[i, j, is_ret] = True, max(right_cherry, down_cherry) + is_cherry
                self.grid[i][j] = is_cherry  # recover status
                return self.memo[i, j, is_ret]
        else:  # returining
            if i == 0 and j == 0:  # reaching final
                return True, 0
            else:
                is_cherry = self.grid[i][j]
                self.grid[i][j] = 0
                left_valid, left_cherry = self.walker_memoization(i, j - 1, True)  # going left
                up_valid, up_cherry = self.walker_memoization(i - 1, j, True)  # going up
                if not left_valid and not up_valid:
                    self.memo[i, j, is_ret] = False, 0
                elif left_valid and not up_valid:
                    self.memo[i, j, is_ret] = True, left_cherry + is_cherry
                elif not left_valid and up_valid:
                    self.memo[i, j, is_ret] = True, up_cherry + is_cherry
                else:
                    self.memo[i, j, is_ret] = True, max(left_cherry, up_cherry) + is_cherry
                self.grid[i][j] = is_cherry
                return self.memo[i, j, is_ret]

    def test(self):
        grid = [[0, 1, -1],
                [1, 0, -1],
                [1, 1,  1]]
        print(self.cherry_pickup_recursion_with_memoization(grid))


Solution().test()
