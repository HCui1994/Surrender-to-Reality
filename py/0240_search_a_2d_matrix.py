"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example:
Consider the following matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.
Given target = 20, return false.
"""


class Solution(object):
    def search_matrix_brutal(self, matrix, target):
        for row in matrix:
            for element in row:
                if element == target:
                    return True
        return False

    def search_matrix_divide_conquer(self, matrix, target):
        """
        考虑矩阵
        | A B |
        | C D |
        A B C D 右下角元素分别为 a b c d
        a > A, a < D
        b > A, B
        c > A, C
        d > A, B, C, D
        考虑 target 所在区域
        case1：target < a，之可能在 A 中
        case2：target > a, b, c and target < d，只可能在 D 中
        case3：可能在 B，C 中，需要创建分支进行 搜索
        """
        if not matrix or not matrix[0]:
            return False
        self.matrix = matrix
        self.target = target
        return self.divide_conquer_helper(top_left_i=0,
                                          top_left_j=0,
                                          bottom_right_i=len(matrix) - 1,
                                          bottom_right_j=len(matrix[0]) - 1)

    # def divide_conquer_helper(self, top_left_i, top_left_j, bottom_right_i, bottom_right_j):
    #     if bottom_right_i - top_left_i < 2 and bottom_right_j - top_left_j < 2:
    #         if self.matrix[top_left_i][top_left_j] == self.target or \
    #            self.matrix[top_left_i][bottom_right_j] == self.target or \
    #            self.matrix[bottom_right_i][top_left_j] == self.target or \
    #            self.matrix[bottom_right_i][bottom_right_j] == self.target:
    #             return True
    #         else:
    #             return False
    #     ai, aj = top_left_i, top_left_j
    #     bi, bj = top_left_i, (top_left_j + bottom_right_j) // 2
    #     ci, cj = top_left_i, bottom_right_j
    #     di, dj = (top_left_i + bottom_right_i) // 2, top_left_j
    #     ei, ej = (top_left_i + bottom_right_i) // 2, (top_left_j +
    #                                                   bottom_right_j) // 2
    #     fi, fj = (top_left_i + bottom_right_i) // 2, bottom_right_j
    #     gi, gj = bottom_right_i, top_left_j
    #     hi, hj = bottom_right_i, (top_left_j + bottom_right_j) // 2
    #     ii, ij = bottom_right_i, bottom_right_j

    #     a, b, c, d, e, f, g, h, i = self.matrix[ai][aj], self.matrix[bi][bj], self.matrix[ci][cj], self.matrix[di][
    #         dj], self.matrix[ei][ej], self.matrix[fi][fj], self.matrix[gi][gj], self.matrix[hi][hj], self.matrix[ii][ij]
    #     # print(a, b, c)
    #     # print(d, e, f)
    #     # print(g, h, i)
    #     if self.target < a or self.target > i:
    #         return False
    #     if self.target == a or \
    #        self.target == b or \
    #        self.target == c or \
    #        self.target == d or \
    #        self.target == e or \
    #        self.target == f or \
    #        self.target == g or \
    #        self.target == h or \
    #        self.target == i:
    #         return True
    #     return self.divide_conquer_helper(ai, aj, ei, ej) or \
    #         self.divide_conquer_helper(bi, bj, fi, fj) or \
    #         self.divide_conquer_helper(di, dj, hi, hj) or \
    #         self.divide_conquer_helper(ei, ej, ii, ij)

    def divide_conquer_helper(self, top_left_i, top_left_j, bottom_right_i, bottom_right_j):
        # print(top_left_i, top_left_j, bottom_right_i, bottom_right_j)
        if bottom_right_i - top_left_i < 2 and bottom_right_j - top_left_j < 2:
            return self.matrix[top_left_i][top_left_j] == self.target or \
                self.matrix[top_left_i][bottom_right_j] == self.target or \
                self.matrix[bottom_right_i][top_left_j] == self.target or \
                self.matrix[bottom_right_i][bottom_right_j] == self.target
        ai, aj = top_left_i, top_left_j
        bi, bj = top_left_i, (top_left_j + bottom_right_j) // 2
        ci, cj = top_left_i, bottom_right_j
        di, dj = (top_left_i + bottom_right_i) // 2, top_left_j
        ei, ej = (top_left_i + bottom_right_i) // 2, (top_left_j +
                                                      bottom_right_j) // 2
        fi, fj = (top_left_i + bottom_right_i) // 2, bottom_right_j
        gi, gj = bottom_right_i, top_left_j
        hi, hj = bottom_right_i, (top_left_j + bottom_right_j) // 2
        ii, ij = bottom_right_i, bottom_right_j

        a, b, c, d, e, f, g, h, i = self.matrix[ai][aj], self.matrix[bi][bj], self.matrix[ci][cj], self.matrix[di][
            dj], self.matrix[ei][ej], self.matrix[fi][fj], self.matrix[gi][gj], self.matrix[hi][hj], self.matrix[ii][ij]
        # print(a, b, c)
        # print(d, e, f)
        # print(g, h, i)
        # print("    ")
        if self.target < a or self.target > i:
            return False
        if self.target == a or \
           self.target == b or \
           self.target == c or \
           self.target == d or \
           self.target == e or \
           self.target == f or \
           self.target == g or \
           self.target == h or \
           self.target == i:
            return True

        res = False
        if self.target > a and self.target < e:
            res = res or self.divide_conquer_helper(
                ai, aj, ei, ej)
        if self.target > b and self.target < f:
            res = res or self.divide_conquer_helper(
                bi, bj, fi, fj)
        if self.target > d and self.target < h:
            res = res or self.divide_conquer_helper(
                di, dj, hi, hj)
        if self.target > e and self.target < i:
            res = res or self.divide_conquer_helper(
                ei, ej, ii, ij)
        return res

    def search_matrix_binary_search(self, matrix, target):
        """
        假设 matrix 非空
        遍历矩阵的对角线，对对角线元素所在的行列上进行二分搜索
        """
        if not matrix or not matrix[0]:
            return False
        for diag_idx in range(min(len(matrix), len(matrix[0]))):
            if self.binary_search(matrix, target, diag_idx, searching_col=True) or \
               self.binary_search(matrix, target, diag_idx, searching_col=False):
                return True
        return False

    def binary_search(self, matrix, target, diag_idx, searching_col):
        """
        注意优化：low = diag_idx
        可以视为将矩阵分为 | A B |
                        | C D |
        四个部分。
        当前正在搜索的是 四个部分交界处的一行和一列
        但是每次只需考虑 D 的两条边，无需考虑 剩下的两条边
        因为如果 target 在剩下的两条边之中，则在之前的循环中就已经被找到并返回结果
        """
        # low = 0
        # 优化：
        low = diag_idx
        high = len(matrix[0]) - 1 if searching_col else len(matrix) - 1

        while high >= low:
            mid = (low + high) // 2
            if searching_col:
                if matrix[diag_idx][mid] < target:
                    low = mid + 1
                elif matrix[diag_idx][mid] > target:
                    high = mid - 1
                else:
                    return True
            else:
                if matrix[mid][diag_idx] < target:
                    low = mid + 1
                elif matrix[mid][diag_idx] > target:
                    high = mid - 1
                else:
                    return True

    def search_matrix_space_reduction(self, matrix, target):
        pass

    def test(self):
        matrix = [[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20],
                  [21, 22, 23, 24, 25]]
        target = 19
        ans = self.search_matrix_binary_search(matrix, target)
        print(ans)


Solution().test()
