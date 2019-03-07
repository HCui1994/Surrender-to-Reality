"""
On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  
These are given as characters 'R', '.', 'B', and 'p' respectively. 
Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: 
it chooses one of four cardinal directions (north, east, west, and south), 
then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  
Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.

Example 1:

Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: 
In this example the rook is able to capture all the pawns.
Example 2:

Input: [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 0
Explanation: 
Bishops are blocking the rook to capture any pawn.

Example 3:

Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: 
The rook can capture the pawns at positions b5, d6 and f5.
"""


class Solution(object):
    def num_rook_captures(self, board):
        # find Rook
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    cnt = 0
                    for r in range(i - 1, -1, -1):
                        if board[r][j] == '.':
                            continue
                        elif board[r][j] == 'p':
                            cnt += 1
                            break
                        else:
                            break
                    for r in range(i + 1, 8, +1):
                        if board[r][j] == '.':
                            continue
                        elif board[r][j] == 'p':
                            cnt += 1
                            break
                        else:
                            break
                    for c in range(j - 1, -1, -1):
                        if board[i][c] == '.':
                            continue
                        elif board[i][c] == 'p':
                            cnt += 1
                            break
                        else:
                            break
                    for c in range(j + 1, 8, +1):
                        if board[i][c] == '.':
                            continue
                        elif board[i][c] == 'p':
                            cnt += 1
                            break
                        else:
                            break
                    return cnt

    def test(self):
        board = [[".", ".", ".", ".", ".", ".", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."], [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "B", "R", "B", "p", ".", "."],
                 [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]
        print(self.num_rook_captures(board))


Solution().test()
