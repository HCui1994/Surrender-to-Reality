
"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
    [1,1,1],
    [1,0,1],
    [1,1,1]
]
Output: 
[
    [1,0,1],
    [0,0,0],
    [1,0,1]
]
Example 2:

Input: 
[
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
]
Output: 
[
    [0,0,0,0],
    [0,4,5,0],
    [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""


class Solution(object):
    def set_zeros(self, matrix: [[int]]) -> None:
        if not matrix or not matrix[0]:
            return

        self.matrix = matrix
        self.m, self.n = len(matrix), len(matrix[0])
        self._mark()
        self._set_zero()

    def _mark(self):
        for i in range(self.m):
            for j in range(self.n):
                if self.matrix[i][j] == 0:
                    for k in range(self.m):
                        if self.matrix[k][j] != 0:
                            self.matrix[k][j] = '#'
                    for k in range(self.n):
                        if self.matrix[i][k] != 0:
                            self.matrix[i][k] = '#'

    def _set_zero(self):
        for i in range(self.m):
            for j in range(self.n):
                if self.matrix[i][j] == '#':
                    self.matrix[i][j] = 0

    def test(self):
        matrix = [
            [0, 1, 2, 0],
            [3, 4, 5, 2],
            [1, 3, 1, 5]
        ]
        self.set_zeros(matrix)
        print(matrix)


Solution().test()
