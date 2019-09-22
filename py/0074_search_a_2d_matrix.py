"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""


class Solution(object):
    def search_matrix(self, matrix: [[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        if matrix[0][0] > target or matrix[m - 1][n - 1] < target:
            return False

        row = self.lower_bound([matrix[i][0] for i in range(m)], target) - 1
        print(row)
        col = self.lower_bound(matrix[row], target) - 1
        print(col)
        return matrix[row][col] == target

    def lower_bound(self, arr, target):
        low, high = 0, len(arr)
        while low < high:
            mid = low + (high - low) // 2
            if arr[mid] <= target:
                low = mid + 1
            else:
                high = mid
        return low

    def test(self):
        matrix = [
            [1,   3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        target = 13

        print(self.search_matrix(matrix, target))


Solution().test()
