"""
A Tic-Tac-Toe board is given as a string array board. 
Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.
The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:
1.  Players take turns placing characters into empty squares (" ").
2.  The first player always places "X" characters, while the second player always places "O" characters.
3.  "X" and "O" characters are always placed into empty squares, never filled ones.
4.  The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
5.  The game also ends if all squares are non-empty.
6.  No more moves can be played if the game is over.

Example 1:
Input: board = ["O  ", "   ", "   "]
Output: false
Explanation: The first player always plays "X".

Example 2:
Input: board = ["XOX", " X ", "   "]
Output: false
Explanation: Players take turns making moves.

Example 3:
Input: board = ["XXX", "   ", "OOO"]
Output: false

Example 4:
Input: board = ["XOX", "O O", "XOX"]
Output: true

Note:
1.  board is a length-3 array of strings, where each string board[i] has length 3.
2.  Each board[i][j] is a character in the set {" ", "X", "O"}.
"""

class Solution:
    def valid_tic_tack_toe(self, board):
        """
        1.  查看 X O 的数目
        2.  查看有多少个制胜pattern
        """
        def validTicTacToe(self, board):
        cnt_x, cnt_o = 0, 0
        for i in range(3):
            for j in range(3):
                cnt_o += board[i][j] == 'O'
                cnt_x += board[i][j] == 'X'
        print(cnt_x, cnt_o)
        if cnt_o not in {cnt_x, cnt_x - 1}:
            return False
        
        def _win(player):
            for i in range(3):
                if all(board[i][j] == player for j in range(3)):
                    return True
                if all(board[j][i] == player for j in range(3)):
                    return True
            if all(board[i][i] == player for i in range(3)):
                return True
            if all(board[i][2 - i] == player for i in range(3)):
                return True
            return False
            
        if _win('X'):
            if cnt_o == cnt_x:
                return False
            else:
                return True
        if _win('O'):
            if cnt_o == cnt_x - 1:
                return False
            else:
                return True
        return True

    def test(self):
        board = ["XXX","OOX","OOX"]
        print(self.valid_tic_tack_toe(board))

Solution().test()