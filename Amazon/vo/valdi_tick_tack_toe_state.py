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
        