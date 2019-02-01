"""
On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. 
The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. 
Return the probability that the knight remains on the board after it has stopped moving.

Example:
Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
 
Note:
N will be between 1 and 25.
K will be between 0 and 100.
The knight always initially starts on the board.
"""


class Solution(object):
    def knight_probability(self, n, k, r, c):
        self.n = n
        self.memo = {}
        print(self.jump(r, c, k))

    def jump(self, i, j, k):
        if i < 0 or j < 0 or i >= self.n or j >= self.n:
            return 0
        if k == 0:
            return 1
        if (i, j, k) in self.memo:
            return self.memo[i, j, k]
        di, dj = [1, 2, 2, 1, -1, -2, -2, -1], [-2, -1, 1, 2, 2, 1, -1, -2]
        posibility = 0
        for d in range(8):
            ii, jj = i + di[d], j + dj[d]
            posibility += self.jump(ii, jj, k - 1)
        posibility /= 8
        self.memo[i, j, k] = posibility
        return self.memo[i, j, k]

    def test(self):
        self.knight_probability(3, 2, 0, 0)


Solution().test()
