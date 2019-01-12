"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
Example 1:
Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:
Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:
1.  A Sudoku board (partially filled) could be valid but is not necessarily solvable.
2.  Only the filled cells need to be validated according to the mentioned rules.
3.  The given board contain only digits 1-9 and the character '.'.
4.  The given board size is always 9x9.
"""


class Solution(object):
    def is_valid_sudoku(self, board):
        col_memo = {x : set() for x in range(9)}
        row_memo = {x : set() for x in range(9)}
        box_memo = {x : set() for x in range(9)}

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in row_memo[row]:
                    return False
                else:
                    row_memo[row].add(board[row][col])
                if board[row][col] in col_memo[col]:
                    return False
                else:
                    col_memo[col].add(board[row][col])
                if board[row][col] in box_memo[row // 3 * 3 + col // 3]:
                    return False
                else:
                    box_memo[row // 3 * 3 + col // 3].add(board[row][col])
        return True

    def test(self):
        board = [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
        print(self.is_valid_sudoku(board))


Solution().test()