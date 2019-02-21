"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""
import copy
import numpy as np

class Solution(object):
    def solve_queens(self, n):
        self.board = [['.' for _ in range(n)] for _ in range(n)]
        self.n = n
        self.res = []
        self.solver(0)
        return self.res

    def solver(self, row):
        if row == self.n:
            self.res.append(["".join(row) for row in self.board])
            return
        for col in range(self.n):
            # print(row, col)
            if self.check(row, col):
                # print(row, col)
                self.board[row][col] = 'Q'
                self.solver(row + 1)
                self.board[row][col] = '.'

    def check(self, row, col):
        print(row, col)
        for offset in range(1, row + 1):
            if self.board[row - offset][col] == 'Q':
                return False
            if col - offset >= 0 and self.board[row - offset][col - offset] == 'Q':
                return False
            if col + offset < self.n and self.board[row - offset][col + offset] == 'Q':
                return False
        return True





    def test(self):
        n = 4
        self.solve_queens(n)


Solution().test()
