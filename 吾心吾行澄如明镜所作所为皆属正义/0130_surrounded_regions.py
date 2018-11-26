"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. 
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""
import numpy as np
class Solution:
    def flip_1(self, board):
        """
        dfs, 遇到 O 就变为 X，
        但如果最终遍历到边缘，在回溯时，将 X 变回 O

        WA
        """
        if not board or not board[0]:
            return
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    self._traversal_1(board, i, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if board[i][j] == '$':
                    board[i][j] = 'O'
        print("==========")
        print(np.array(board))
        print("==========")
        print(np.array([["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]]))
    
    def _traversal_1(self, board, i, j):
        if board[i][j] == 'O':
            board[i][j] = '$'
            if i == len(board) - 1 or i == 0 or j == len(board[0]) - 1 or j == 0:
                print(i, j, "****")
                print(np.array(board))
                return True
            else:
                board[i][j] = 'X'
                di = [1, -1, 0, 0]
                dj = [0, 0, 1, -1]
                flag = False
                for direction in range(4):
                    ii, jj = i + di[direction], j + dj[direction]
                    if ii >= 0 and ii < len(board) and jj >= 0 and jj < len(board[0]):
                        flag = flag or self._traversal_1(board, ii, jj)
                    if flag:
                        board[i][j] = '$'
                    print(i, j, flag, "====")
                    print(np.array(board))
                return flag
        return False


    def flip_2(self, board):
        """
        从边缘的 O 开始 dfs，遇到 O 就变为 $
        最终，与边缘接壤的全部是 $，其余的 O 全部变为 X
        """
        if not board or not board[0]:
            return
        for i in range(len(board)):
            self._traversal_2(board, i, 0)
            self._traversal_2(board, i, len(board[0]) - 1)
        for j in range(len(board[0])):
            self._traversal_2(board, 0, j)
            self._traversal_2(board, len(board) - 1, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = 'X'
                if board[i][j] == '$':
                    board[i][j] = 'O'

    def _traversal_2(self, board, i, j):
        if board[i][j] == "O":
            board[i][j] = "$"
            di = [1, -1, 0, 0]
            dj = [0, 0, 1, -1]
            for direction in range(4):
                ii, jj = i + di[direction], j + dj[direction]
                if ii >= 0 and ii < len(board) and jj >= 0 and jj < len(board[0]):
                    self._traversal_2(board, ii, jj)

    def test(self):
        board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
        expect = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
        
        print(np.array(board))
        print("====")
        print(np.array(expect))
        
        self.flip_2(board)
        print("====")
        print(np.array(board))



soln = Solution()
soln.test()