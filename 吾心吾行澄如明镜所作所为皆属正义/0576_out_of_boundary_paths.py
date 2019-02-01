"""
There is an m by n grid with a ball. 
Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). 
However, you can at most move N times. 
Find out the number of paths to move the ball out of grid boundary. 
The answer may be very large, return it after mod 109 + 7.

Example 1:
Input: m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6

Example 2:
Input: m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12

Note:
Once you move the ball out of boundary, you cannot move it back.
The length and height of the grid is in range [1,50].
N is in range [0,50].
"""

class Solution(object):
    def find_path(self, m, n, k, i, j):
        self.m, self.n = m, n
        self.memo = {}
        return self.kick(i, j, k)

    def kick(self, i, j, k):
        if i < 0 or j < 0 or i >= self.m or j >= self.n:
            return 1
        if k == 0:
            return 0
        if (i, j, k) in self.memo:
            return self.memo[i, j, k]
        di, dj = [0, 0, 1, -1], [1, -1, 0, 0]
        npaths = 0
        for d in range(4): 
            ii, jj = i + di[d], j + dj[d]
            npaths += self.kick(ii, jj, k - 1) % 1000000007
        self.memo[i, j, k] = npaths % 1000000007
        return self.memo[i, j, k]