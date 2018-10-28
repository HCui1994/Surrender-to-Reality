class Solution:
    def __init__(self):
        self._n = 0
        self._total_result = []

    def generateParenthesis(self, n):
        self._n = n
        if self._n == 0:
            return []
        one_result = "("        # 第一个肯定是左括号
        self.generator(left=1, right=0, one_result=one_result)
        return self._total_result

    def generator(self, left, right, one_result):
        if left < self._n:      # 如果左括号的数量小于n （根据逻辑，右括号肯定也小于n）
            if left > right:    # 如果左括号多于右括号，既可以添加左括号，也可以添加右括号
                self.generator(left+1, right, one_result+"(")   #创建一个加左括号的分支
                self.generator(left, right+1, one_result+")")   #创建一个加右括号的分支
            else:
                self.generator(left+1, right, one_result+"(")   #如果左括号等于右括号，只能加右括号
        elif right < self._n:   # 如果左括号已经有n个，但是右括号还不够n个
            self.generator(left, right+1, one_result+")")       # 剩下的全部是右括号分支
        else:                   # 如果左右括号都达到了n个
            self._total_result.append(one_result)   # 将该分支添加到结果集，返回
                


solution = Solution()
n = 3
print(solution.generateParenthesis(n))


        