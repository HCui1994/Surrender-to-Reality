import numpy as np
import time


class Solution:
    def solve_sudoku(self, board):
        self.board = board
        self.filler()
        # print(self.board)

    def filler(self):
        print(np.array(self.board))
        # time.sleep(0.1)
        print()
        i, j = self.find_blank()
        if i == -1 and j == -1:
            return True
        for digit in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if not self.check(i, j, digit):
                continue
            self.board[i][j] = digit
            if self.filler():
                return True
            self.board[i][j] = '.'
        return False

    def find_blank(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '.':
                    return i, j
        return -1, -1

    def check(self, i, j, val):
        row_seen = set([self.board[i][jj] for jj in range(9)]) - set('.')
        col_seen = set([self.board[ii][j] for ii in range(9)]) - set('.')
        block_seen = set([self.board[ii][jj] for ii in range(
            i // 3 * 3, i // 3 * 3 + 3) for jj in range(j // 3 * 3, j // 3 * 3 + 3)])
        return False if val in row_seen or val in col_seen or val in block_seen else True


    def solve_sudoku_speed_boost(self, board):
        self.board = board
        self.row_seen = {x: set() for x in range(9)}
        self.col_seen = {x: set() for x in range(9)}
        self.block_seen = {x: set() for x in range(9)}
        self.blanks = []
        for i in range(9):
            for j in range(9):
                digit = board[i][j]
                if digit == '.':
                    self.blanks.append((i, j))
                else:
                    self.row_seen[i].add(digit)
                    self.col_seen[j].add(digit)
                    self.block_seen[i // 3 * 3 + j // 3].add(digit)
        self.filler_speed_boost()
        
    def filler_speed_boost(self):
        print(np.array(self.board))
        
        time.sleep(0.2)
        if not self.blanks:
            return True
        i, j = self.blanks.pop()
        print(i, j)
        for digit in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if digit in self.row_seen[i] or digit in self.col_seen[j] or digit in self.block_seen[i // 3 * 3 + j // 3]:
                continue
            self.board[i][j] = digit
            self.row_seen[i].add(digit)
            self.col_seen[j].add(digit)
            self.block_seen[i // 3 * 3 + j // 3].add(digit)
            if self.filler_speed_boost():
                return True
            self.board[i][j] = '.'
            self.row_seen[i].remove(digit)
            self.col_seen[j].remove(digit)
            self.block_seen[i // 3 * 3 + j // 3].remove(digit)
        self.blanks.append((i, j))
        return False

    def test(self):
        board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                 [".", "9", "8", ".", ".", ".", ".", "6", "."],
                 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                 [".", "6", ".", ".", ".", ".", "2", "8", "."],
                 [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        self.solve_sudoku_speed_boost(board)


Solution().test()
