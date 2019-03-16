"""
On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved.
If it is impossible for the state of the board to be solved, return -1.

Examples:
Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.

Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]

Input: board = [[3,2,4],[1,5,0]]
Output: 14

Note:
board will be a 2 x 3 array as described above.
board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].
"""
from copy import deepcopy
import numpy as np


class Solution(object):

    def sliding_window_single_bfs(self, board):
        def _encode(board):
            key = ""
            for r in range(2):
                for c in range(3):
                    key += str(board[r][c])
            return key

        def _decode(key):
            board = [[0 for _ in range(3)] for _ in range(2)]
            for i, num in enumerate(key):
                board[i // 3][i % 3] = int(num)
            return board

        def _find_zero(board):
            for r in range(2):
                for c in range(3):
                    if board[r][c] == 0:
                        return r, c

        start = _encode(board)
        if start == "123450":
            return 0
        queue = [start]
        moves = 0
        visited = set([start])
        while queue:
            temp_queue = set()
            for state_key in queue:
                visited.add(state_key)
                state_board = _decode(state_key)
                i, j = _find_zero(state_board)
                di, dj = [0, 0, -1, 1], [-1, 1, 0, 0]
                for k in range(4):
                    ii, jj = i + di[k], j + dj[k]
                    if not (0 <= ii < 2 and 0 <= jj < 3):
                        continue
                    new_state_board = deepcopy(state_board)
                    new_state_board[ii][jj] = state_board[i][j]
                    new_state_board[i][j] = state_board[ii][jj]
                    new_state_key = _encode(new_state_board)
                    if new_state_key in visited:
                        continue
                    if new_state_key == "123450":
                        return moves + 1
                    temp_queue.add(new_state_key)
            queue = temp_queue
            moves += 1
        return -1

    def sliding_pizzle_double_bfs(self, board):
        def _encode(board):
            key = ""
            for i in range(2):
                for j in range(3):
                    key += str(board[i][j])
            return key

        def _decode(key):
            board = [[0 for _ in range(3)] for _ in range(2)]
            for i, ele in enumerate(key):
                board[i // 3][i % 3] = int(ele)
            return board

        def _find_zero(board):
            for i in range(2):
                for j in range(3):
                    if board[i][j] == 0:
                        return i, j

        begin = _encode(board)
        end = "123450"
        if begin == end:
            return 0

        begin_queue, end_queue = set(), set()
        begin_queue.add(begin)
        end_queue.add(end)
        moves = 0

        visited = set([begin, end])
        while begin_queue and end_queue:

            if len(begin_queue) > len(end_queue):
                begin_queue, end_queue = end_queue, begin_queue

            temp_queue = set()

            for state_key in begin_queue:
                visited.add(state_key)
                state_board = _decode(state_key)
                i, j = _find_zero(state_board)
                di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
                for k in range(4):
                    ii, jj = i + di[k], j + dj[k]
                    if not (0 <= ii < 2 and 0 <= jj < 3):
                        continue
                    new_state_board = deepcopy(state_board)
                    new_state_board[ii][jj] = state_board[i][j]
                    new_state_board[i][j] = state_board[ii][jj]
                    new_state_key = _encode(new_state_board)
                    if new_state_key in end_queue:
                        return moves + 1
                    if new_state_key in visited:
                        continue
                    temp_queue.add(new_state_key)

            moves += 1
            begin_queue = temp_queue

        return -1


if __name__ == '__main__':
    board = [[4, 1, 2], [5, 0, 3]]
    soln = Solution()
    print(soln.sliding_pizzle_double_bfs(board))
