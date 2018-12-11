"""
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""
import numpy as np
class Solution:
    def exist(self, board, word):
        if not board:
            return False
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and self._dfs(board, i, j, m, n, word, 0):
                    print(np.array(board))
                    print("========")
                    return True
        return False


    def _dfs(self, board, i, j, m, n, word, idx):
        if word[idx] != board[i][j]:
            return False
        # 筛选剩余case：word[idx] == board[i][j]
        if idx == len(word) - 1:
            board[i][j] = '#'
            return True
        if idx == len(word):
            return False
        memo = board[i][j]  # 记录 board[i][j]，在结束当前分支的时候还原棋盘状态
        board[i][j] = '#'   # 标记为当前分支下 visited
        di = [1, -1, 0, 0]
        dj = [0, 0, 1, -1]
        for direction in range(4):
            ii, jj = i + di[direction], j + dj[direction]
            if 0 <= ii and ii < m and 0 <= jj and jj < n and self._dfs(board, ii, jj, m, n, word, idx + 1):
                return True
        board[i][j] = memo
        return False
                


    def test(self):
        board =[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
        word = "ABC"
        print(self.exist(board, word))


Solution().test()