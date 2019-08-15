"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
import numpy as np
from enum import Enum

Direction = Enum("Direction", ("up", "down", "left", "right"))


class Solution(object):
    def generate_matrix(self, n: int) -> [[int]]:
        if n == 0:
            return [[]]
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        i = j = 0
        cnt = 0
        fill = 1
        direction = Direction.right
        while fill <= n ** 2:
            matrix[i][j] = fill
            fill += 1
            if direction == Direction.right:
                j += 1
                if j == n or matrix[i][j]:
                    j -= 1
                    i += 1
                    direction = Direction.down
            elif direction == Direction.down:
                i += 1
                if i == n or matrix[i][j]:
                    i -= 1
                    j -= 1
                    direction = Direction.left
            elif direction == Direction.left:
                j -= 1
                if j == -1 or matrix[i][j]:
                    j += 1
                    i -= 1
                    direction = Direction.up
            elif direction == Direction.up:
                i -= 1
                if i == -1 or matrix[i][j]:
                    i += 1
                    j += 1
                    direction = Direction.right

        print(np.array(matrix))
        return matrix


Solution().generate_matrix(4)