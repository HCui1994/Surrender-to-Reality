"""
Give you an integer matrix (with row size n, column size m)，find the longest increasing continuous subsequence in this matrix. 
(The definition of the longest increasing continuous subsequence here can start at any row or column and go up/down/right/left any direction).

Example
Given a matrix:

[
    [1 ,2 ,3 ,4 ,5],
    [16,17,24,23,6],
    [15,18,25,22,7],
    [14,19,20,21,8],
    [13,12,11,10,9]
]
return 25
"""

import numpy as np

class Solution:
    def __init__(self):
        self._memo = None
        self._visited = None
        self._matrix = None
        self._num_row = 0
        self._num_col = 0

    def longest_inc_cont_subseq(self, matrix):
        if not matrix:
            return 0
        self._num_row = len(matrix)
        self._num_col = len(matrix[0])
        self._visited = [[False for _ in range(self._num_col)] for _ in range(self._num_row)]
        self._memo = [[1 for _ in range(self._num_col)] for _ in range(self._num_row)]
        self._matrix = matrix
        max_length = 0
        for i in range(self._num_row):
            for j in range(self._num_col):
                max_length = max(self._dfs(i, j), max_length)
        print(np.array(self._memo))
        return max_length

    def _dfs(self, i, j):
        if self._visited[i][j]:  # 每个节点仅被访问一次
            return self._memo[i][j]
        current_max = 1
        di = [1, -1, 0, 0]
        dj = [0, 0, -1, 1]
        for idx in range(4):
            ii = i + di[idx]
            jj = j + dj[idx]
            if ii >=0 and ii < self._num_row and jj >=0 and jj < self._num_col:
                if self._matrix[ii][jj] > self._matrix[i][j]:
                    current_max = max(current_max, self._dfs(ii, jj) + 1)
        # 第一个完成访问的节点，必然是拥有最大值的节点，因为其“最深”
        self._visited[i][j] = True
        self._memo[i][j] = current_max
        print(self._matrix[i][j])
        return current_max
        

matrix = [
    [1 ,2 ,3 ,4 ,5],
    [16,17,24,23,6],
    [15,18,25,22,7],
    [14,19,20,21,8],
    [13,12,11,10,9]
]

soln = Solution()
ans = soln.longest_inc_cont_subseq(matrix)

print(ans)
