"""
According to the Wikipedia's article: 
"The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
Given a board with m by n cells, each cell has an initial state live (1) or dead (0). 
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

元胞自动机
1.  Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    少于两个临接的元胞将死去
2.  Any live cell with two or three live neighbors lives on to the next generation.
    2 或 3 个临接的元胞将存活
3.  Any live cell with more than three live neighbors dies, as if by over-population.
    多于 3 个邻接的元胞将死去
4.  Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    有恰好 3 个元胞的空位将生出 1 个元胞

Write a function to compute the next state (after one update) of the board given its current state. 
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:
Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

Follow up:
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. 
How would you address these problems?
"""
import numpy as np
class Solution(object):
    def game_of_life(self, board):
        """
        定义卷积操作，卷积核 
        [
            [1, 1, 1]
            [1, 0, 1]
            [1, 1, 1]
        ]
        """
        if not board or not board[0]:
            return board
        h, w = len(board), len(board[0])
        boarder_board = [[0 for _ in range(w + 2)] for _ in range(h + 2)]
        for i in range(h):
            for j in range(w):
                boarder_board[i + 1][j + 1] = board[i][j]
        for i in range(1, h + 1):
            for j in range(1, w + 1):
                # print(i, j)
                flag =  boarder_board[i - 1][j - 1] + \
                        boarder_board[i - 1][j] + \
                        boarder_board[i - 1][j + 1] + \
                        boarder_board[i][j - 1] + \
                        boarder_board[i][j + 1] + \
                        boarder_board[i + 1][j - 1] + \
                        boarder_board[i + 1][j] + \
                        boarder_board[i + 1][j + 1] 
                if flag == 3:
                    board[i - 1][j - 1] = 1
                elif flag == 2:
                    continue
                else:
                    board[i - 1][j - 1] = 0
        return board
    

    def test(self):
        board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
        print(self.game_of_life(board))


Solution().test()