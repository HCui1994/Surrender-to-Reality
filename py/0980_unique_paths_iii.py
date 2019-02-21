"""
On a 2-dimensional grid, there are 4 types of squares:
1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

Example 1:
Input: [[1,0,0,0],
        [0,0,0,0],
        [0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:
Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:
Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 
Note:
1 <= grid.length * grid[0].length <= 20
"""


class Solution(object):
    def unique_paths(self, grid):
        if not grid or not grid[0]:
            return 0
        self.nrows, self.ncols = len(grid), len(grid[0])
        self.grid = grid
        self.visited = set()
        self.non_obstacle = 0
        for i in range(self.nrows):
            for j in range(self.ncols):
                if self.grid[i][j] == 1:
                    self.start = (i, j)
                elif self.grid[i][j] == 0:
                    self.non_obstacle += 1
        return self.walker(self.start[0], self.start[1], -1)

    def walker(self, i, j, counter):
        if self.grid[i][j] == 2:
            # print(self.non_obstacle)
            if counter == self.non_obstacle:
                return 1
            else:
                return 0
        if (i, j) in self.visited:
            return 0
        if self.grid[i][j] == -1:
            return 0
        self.visited.add((i, j))
        di, dj = [1, -1, 0, 0], [0, 0, 1, -1]
        paths = 0
        for direction in range(4):
            ii, jj = i + di[direction], j + dj[direction]
            if ii >= 0 and jj >= 0 and ii < self.nrows and jj < self.ncols:
                paths += self.walker(ii, jj, counter + 1)
        self.visited.remove((i, j))
        return paths

    def test(self):
        print(self.unique_paths([[1, 0, 0, 0],
                                 [0, 0, 0, 0],
                                 [0, 0, 2, -1]]))
    

Solution().test()
