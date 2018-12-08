"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6

SCORE:

"""
import numpy as np  
class Solution(object):
    # def maximal_rectangle_dp(self, matrix):
    #     """
    #     尝试动态规划
    #     memo[i, j]: (int, int) 代表以 i, j 为右下角的最大矩形的 长，宽
    #     难点在于，以 i，j 为右下角，可能有多个同样面积的矩形
    #     有三种可能，以 i, j 为右下角的矩形包含了
    #     1.  i-1, j-1 的矩形
    #     2.  不包含 i-1, j-1 的矩形，包含 i-1, j 的矩形
    #     3.  不包含 i-1, j-1 的矩形，包含 i, j-1 的矩形
    #     """
    #     h, w = len(matrix), len(matrix[0])
    #     memo = [[{"topleft": set(0, 0), 
    #               "width": 0,
    #               "height": 0} 
    #     for _ in range(w + 1)] for _ in range(h + 1)]
    #     # memo[i][j]["height"] 表示以 memo[i][j] 向上数有多少个连续的 “1”
    #     # memo[i][j]["width"] 表示以 memo[i][j] 向左数有多少个连续的 “1”
    #     # memo[i][j]["topleft"] 表示以 memo[i][j] 为右下角，包含 memo[i-1][j-1] 的矩形的 height, width
    #     max_area = 0
    #     for i in range(h):
    #         mi = i + 1
    #         for j in range(w):
    #             mj = j + 1
    #             if matrix[i][j] == "0":
    #                 continue
    #             memo[mi][mj]["height"] = memo[mi - 1][mj]["height"] + 1  # going up
    #             memo[mi][mj]["width"] = memo[mi][mj - 1]["width"] + 1    # going left
    #             for topleft_height, wopleft_width in memo[mi - 1][mj - 1]["topleft"]:
    #     # print(memo)
    #     # print(max_area)
    #     return max_area

    def maximal_rectangle_2(self, matrix):
        """
        类似于 0084 largest rectangle in histogram
        找到每一行为底的 histogram
        """
        if not matrix:
            return 0
        h, w = len(matrix), len(matrix[0])
        for i in range(h):
            for j in range(w):
                matrix[i][j] = int(matrix[i][j])
        hi = h - 1
        inputs = matrix[hi]
        kernel = matrix[hi - 1]
        for idx in range(1, len(matrix)):
            self._conv(matrix[idx], matrix[idx - 1])
        # print(np.array(matrix))
        max_area = 0
        for histogram in matrix:
            max_area = max(max_area, self._largest_rectangle_in_histogram(histogram))
        return max_area

    def _largest_rectangle_in_histogram(self, histogram):
        """
        从左向右找局部极大值，找到后，从右向左计算最大矩形
        """
        histogram = [0] + histogram + [0]
        right_ptr = 0
        max_area = 0
        for right_ptr in range(1, len(histogram) - 1):
            if histogram[right_ptr] > histogram[right_ptr + 1]:
                # 寻找局部极大值
                max_area = max(max_area, histogram[right_ptr])
                min_bin = histogram[right_ptr]
                for left_ptr in range(right_ptr - 1, 0, -1):
                    min_bin = min(min_bin, histogram[left_ptr])
                    max_area = max(max_area, min_bin * (right_ptr - left_ptr + 1))
        # print(max_area)
        return max_area
        
    def _conv(self, inputs, kernel):
        for idx in range(len(inputs)):
            if inputs[idx] and kernel[idx]:
                inputs[idx] += kernel[idx] 

    def test2(self, matrix):
        h, w = len(matrix), len(matrix[0])
        for i in range(h):
            for j in range(w):
                matrix[i][j] = int(matrix[i][j])
        hi = h - 1
        inputs = matrix[hi]
        kernel = matrix[hi - 1]
        # print(np.array(matrix))
        for idx in range(1, len(matrix)):
            self._conv(matrix[idx], matrix[idx - 1])
        # print(np.array(matrix))

    def test(self):
        matrix = [["1","1","1","0","0"],["1","0","1","1","1"], ["1","1","1","1","1"], ["1","0","0","1","0"]]
        print(self.maximal_rectangle_2(matrix))
        


Solution().test()

