"""
Given a grid where each entry is only 0 or 1, find the number of corner rectangles.
A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned rectangle. Note that only the corners need to have the value 1. Also, all four 1s used must be distinct.

Example 1:
Input: grid = 
[[1, 0, 0, 1, 0],
 [0, 0, 1, 0, 1],
 [0, 0, 0, 1, 0],
 [1, 0, 1, 0, 1]]

Output: 1
Explanation: There is only one corner rectangle, with corners grid[1][2], grid[1][4], grid[3][2], grid[3][4].

Example 2:
Input: grid = 
[[1, 1, 1],
 [1, 1, 1],
 [1, 1, 1]]
Output: 9
Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, and one 3x3 rectangle.

Example 3:
Input: grid = 
[[1, 1, 1, 1]]
Output: 0
Explanation: Rectangles must have four distinct corners.
"""


class Solution:
    """cv project，数平行四边形，brutal"""
    def countCornerRectangles(self, grid):
        if not grid:
            return 0
        if len(grid) == 1 or len(grid[0]) == 1:
            return 0
        streets = []
        avenues = []
        m, n = len(grid), len(grid[0])
        count = 0
        for x1 in range(m - 1):
            for x2 in range(x1 + 1, m, +1):
                for y1 in range(n - 1):
                    for y2 in range(y1 + 1, n, +1):
                        if grid[x1][y1] == 1 and grid[x1][y2] == 1 and grid[x2][y1] == 1 and grid[x2][y2] == 1:
                            count += 1
        print(count)


                


    # def countCornerRectangles(self, grid):
    #     """每次新加入一行，增加多少个矩形？"""
    #     if not grid:
    #         return 0
    #     if len(grid) == 1 or len(grid[0]) == 1:
    #         return 0
        



soln = Solution()
grid = [[1, 1, 1],
 [1, 1, 1],
 [1, 1, 1]]
soln.countCornerRectangles(grid)