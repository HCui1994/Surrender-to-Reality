class Solution:
    def maximum_square_brutal(self, matrix):
        """Brutal, TLE ..... """
        max_area = 0
        for y1 in range(len(matrix)):
            for x1 in range(len(matrix[0])):
                for edge in range(1, min(len(matrix)-y1, len(matrix[0])-x1) + 1, +1):
                    # edge 至少为1，至多为 length +1
                    x2 = x1 + edge
                    y2 = y1 + edge
                    # print(x1, y1, x2, y2)
                    area = 0
                    for y in range(y1, y2, +1):
                        for x in range(x1, x2, +1):
                            area += int(matrix[y][x])
                    if area == edge ** 2 and area > max_area:
                        max_area = area
        return max_area

    def maximum_square_dp(self, matrix):
        """
        dp solution
        若某个点是一个正方形的右下角，则其 1.左侧 2.上侧 3.左上侧 三个点一定也是某个正方形的右下角
        初始化就是matrix自身
        """
        matrix = [[int(element) for element in row] for row in matrix]
        # print(matrix[1][3])
        num_row = len(matrix)
        if not num_row:
            return 0
        num_col = len(matrix[0])
        for row in range(1, num_row, +1):
            for col in range(1, num_col, +1):
                if matrix[row][col] == 1:
                    matrix[row][col] = min(matrix[row - 1][col - 1], matrix[row][col - 1], matrix[row - 1][col]) + 1
        # print(matrix)
        max_edge = 0
        for row in range(num_row):
            for col in range(num_col):
                if matrix[row][col] > max_edge:
                    max_edge = matrix[row][col]
        return max_edge ** 2
        # print(max(matrix))



"""
1 1 1 0 1 
1 2 2 1 0
1 2 3 X 0
0 0 0 0 0

X = ? min(2, 3, 1) + 1 = 2
"""



matrix = [["0","0","0"],["0","0","1"],["0","0","0"],["0","0","0"]]
soln = Solution()
ans = soln.maximum_square_dp(matrix)
print(ans)