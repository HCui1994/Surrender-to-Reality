import numpy as np

class Solution(object):
    def rotate(self, matrix):
        """
        first flip, then transpose
        """
        if not matrix:
            return []
        if len(matrix) != len(matrix[0]):
            return matrix

        n = len(matrix)
        # flip
        for col in range(n):
            for row in range(n // 2):
                matrix[row][col], matrix[n - row - 1][col] = matrix[n - row - 1][col], matrix[row][col]
        # transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(np.array(matrix))

    def test(self):
        matrix = [[5, 1, 9, 11],
                  [2, 4, 8, 10],
                  [13, 3, 6, 7],
                  [15, 14, 12, 16]
                  ]
        self.rotate(matrix)


Solution().test()
