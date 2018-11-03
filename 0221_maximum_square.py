"""Brutal! TLE ..... """
class Solution:
    def maximalSquare(self, matrix):
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



class Solution