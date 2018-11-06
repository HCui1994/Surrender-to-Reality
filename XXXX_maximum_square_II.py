"""
Follow Up Maximal Square II
Given a 2D binary matrix filled with 0’s and 1’s, find the largest square which diagonal is all 1 and others is 0.

Notice

Only consider the main diagonal situation.

For example, given the following matrix:

1 0 1 0 0
1 0 0 1 0
1 1 0 0 1
1 0 0 1 0

Return 9
"""
class Solution:
    def maximum_square(self, matrix):
        num_row = len(matrix)
        if not num_row:
            return 0
        num_col = len(matrix[0])
        for row in range(1, num_row, +1):
            for col in range(1, num_col, +1):
                if matrix[row][col] == 1 and matrix[row - 1][col - 1] != 0:
                    diag_length = matrix[row - 1][col - 1]
                    extend_flag = True
                    for idx in range(1, diag_length + 1, +1):
                        if matrix[row][col - idx] != 0 or matrix[row - 1][col] != 0:
                            extend_flag = False
                            break
                    if extend_flag:
                        matrix[row][col] = matrix[row - 1][col - 1] + 1
        max_diagnal = 0
        for row in matrix:
            for element in row:
                max_diagnal = max(max_diagnal, element)
        return max_diagnal ** 2

        
                    
                
"""
1 0 1 0 0
1 0 0 2 0
1 1 0 0 X
1 0 0 1 0

X = ? 
"""



matrix = [
    [1, 0, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 1, 0, 0, 1],
    [1, 0, 0, 1, 0]
]

soln = Solution()
ans = soln.maximum_square(matrix)
print(ans)