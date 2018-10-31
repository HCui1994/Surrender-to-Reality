class Solution:
    def maxAreaOfIsland(self, grid):
        """ BSF Solution """
        if not grid:
            return 0
        max_area = 0
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curr_area = 0   
                if grid[i][j] == 1: # find isolated islands
                    grid[i][j] = -1
                    queue.append((i, j))
                while queue:        # from the first piece of isolated island, sniff the remaining pieces
                    row, col = queue.pop(0)  
                    # row, col = queue.pop()    # this is to switch to a DFS_iter version. Of course, the queue becomes a stack
                                                # pop() is faster than pop(0), so DFS_iter maybe faster?
                    curr_area += 1
                    if col + 1 < len(grid[0]) and grid[row][col+1] == 1:
                        grid[row][col+1] = -1
                        queue.append((row, col+1))
                    if row + 1 < len(grid) and grid[row+1][col] == 1:
                        grid[row+1][col] = -1
                        queue.append((row+1, col))
                    if col- 1 >=0 and grid[row][col-1] == 1:
                        grid[row][col-1] = -1
                        queue.append((row, col-1))
                    if row - 1 >= 0 and grid[row-1][col] == 1:
                        grid[row-1][col] = -1
                        queue.append((row-1, col))
                    grid[row][col] = 0
                if curr_area > max_area:
                    max_area = curr_area

        return max_area

    def maxAreaOfIsland_DFS(self, grid):
        """ DFS Solution """
        if len(grid) == 0:
            return 0
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                curr_area = self._dfs(grid=grid, row=row, col=col, curr_area=0)
                if curr_area > max_area:
                    max_area = curr_area
        return max_area
    
    def _dfs(self, grid, row, col, curr_area):
        if row < len(grid) and col < len(grid[0]) and row >=0 and col >= 0:
            if grid[row][col] == 0:
                return curr_area
            else:
                grid[row][col] = 0
                return self._dfs(grid, row+1, col, curr_area) + self._dfs(grid, row, col+1, curr_area) + self._dfs(grid, row-1, col, curr_area) + self._dfs(grid, row, col-1, curr_area) + 1
        else:
            return 0


solution = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(solution.maxAreaOfIsland_DFS(grid))