import numpy as np
import time


class Solution:
    def solveSudoku(self, board):
        self.init_board = self.success_board = board
        self.board = board
        self.col_seen = {x: set() for x in range(9)}
        self.row_seen = {x: set() for x in range(9)}
        self.block_seen = {x: set() for x in range(9)}
        self.blank = set()
        for i in range(9):
            for j in range(9):
                digit = board[i][j]
                if digit == '.':
                    start = (i, j)
                    self.blank.add((i, j))
                else:
                    if digit in self.row_seen[i] or digit in self.col_seen[j] or digit in self.block_seen[i // 3 * 3 + j // 3]:
                        return
                    else:
                        self.row_seen[i].add(digit)
                        self.col_seen[j].add(digit)
                        self.block_seen[i // 3 * 3 + j // 3].add(digit)
        self.visited = set()
        return self.filler(start[0], start[1])
        

    def filler(self, i, j):
        if (i, j) not in self.blank:
            return False
        self.blank.remove((i, j))

        all_digits = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        occupied_row_digits = self.row_seen[i]
        occupied_col_digits = self.col_seen[j]
        occupied_block_digits = self.block_seen[i // 3 * 3 + j // 3]
        available_digits = all_digits - occupied_row_digits - occupied_col_digits - occupied_block_digits
        if not available_digits:
            self.blank.add((i, j))
            return False
        if len(available_digits) == 1 and not self.blank:
            self.board[i][j] = available_digits.pop()
            self.success_board = self.board
            return True
        for digit in available_digits:
            self.row_seen[i].add(digit)
            self.col_seen[j].add(digit)
            self.block_seen[i // 3 * 3 + j // 3]
            self.board = digit
            for ii, jj in self.blank:
                self.row_seen[i].add(digit)
                self.col_seen[j].add(digit)
                self.block_seen[i // 3 * 3 + j // 3].add(digit)
                if self.filler(ii, jj):
                    return True
                self.row_seen[i].remove(digit)
                self.col_seen[j].remove(digit)
                self.block_seen[i // 3 * 3 + j // 3].remove(digit)
        self.blank.add((i, j))
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
        print(self.solveSudoku(board))


Solution().test()
