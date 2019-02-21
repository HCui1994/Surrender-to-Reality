class Solution:
    def spiralOrder(self, matrix):
        
        m = len(matrix)
        if m == 0:
            return []
        if m == 1:
            return matrix[0]
        result = []
        flag = "right"
        print("SHIS")
        while not len(matrix) == 0 and not len(matrix[0]) == 0:
            if flag == "right":
                result += matrix.pop(0)
                flag = "down"
            elif flag == "down":
                for row in matrix:
                    result.append(row.pop())
                flag = "left"
            elif flag == "left":
                result += matrix.pop()[::-1]
                flag = "up"
            else:
                for row in matrix[::-1]:
                    result.append(row.pop(0))
                flag = "right"
                
        return result

print("shit")
solution = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(solution.spiralOrder(matrix))
