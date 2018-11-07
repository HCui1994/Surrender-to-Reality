import numpy as np
class Solution:
    def __init__(self):
        self._num_of_island = 0

    def num_islands_dfs(self, grid):
        """
        DFS Solution
        """
        if not grid:
            return 0
        num_row, num_col = len(grid), len(grid[0])
        for i in range(num_row):
            for j in range(num_col):
                if grid[i][j] == "1":
                    self._dfs(grid, i, j)
                    grid[i][j] = 0
                    self._num_of_island += 1
        return self._num_of_island

    def _dfs(self, grid, i, j):
        if i == len(grid) or j == len(grid[0]) or i < 0 or j < 0:
            return
        if grid[i][j] == "1":
            grid[i][j] = "-1"  # 注意，采用preorder，先设置“已访问”，否则会找不到出口
            self._dfs(grid, i + 1, j)
            self._dfs(grid, i, j + 1)
            self._dfs(grid, i - 1, j)
            self._dfs(grid, i, j - 1)
            grid[i][j] = "0"

    def num_islands_bfs(self, grid):
        """
        BFS Solution
        """
        if not grid:
            return 0
        queue = []
        num_row, num_col = len(grid), len(grid[0])
        num_of_island = 0
        for i in range(num_row):
            for j in range(num_col):
                if grid[i][j] == "1":
                    queue.append((i, j))
                    grid[i][j] = "-1"
                    while queue:
                        curr_i, curr_j = queue.pop(0)
                        if curr_i + 1 < num_row and grid[curr_i + 1][curr_j] == "1":
                            queue.append((curr_i + 1, curr_j))
                            grid[curr_i + 1][curr_j] = "-1"
                        if curr_j + 1 < num_col and grid[curr_i][curr_j + 1] == "1":
                            queue.append((curr_i, curr_j + 1))
                            grid[curr_i][curr_j + 1] = "-1"
                        if curr_i - 1 >= 0 and grid[curr_i - 1][curr_j] == "1":
                            queue.append((curr_i - 1, curr_j))
                            grid[curr_i - 1][curr_j] = "-1"
                        if curr_j - 1 >= 0 and grid[curr_i][curr_j - 1] == "1":
                            queue.append((curr_i, curr_j - 1))
                            grid[curr_i][curr_j - 1] = "-1"
                        grid[curr_i][curr_j] = "0"
                    num_of_island += 1
        return num_of_island
                        
                        



soln = Solution()
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
ans = soln.num_islands_bfs(grid)
print(ans)
        