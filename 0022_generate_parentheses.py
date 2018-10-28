class Solution:
    def __init__(self):
        self._n = 0
        self._total_result = []

    def generateParenthesis(self, n):
        self._n = n
        if self._n == 0:
            return []
        one_result = "("
        self.generator(left=1, right=0, one_result=one_result)
        return self._total_result

    def generator(self, left, right, one_result):
        if left < self._n:
            if left > right:
                self.generator(left+1, right, one_result+"(")
                self.generator(left, right+1, one_result+")")
            else:
                self.generator(left+1, right, one_result+"(")
        elif right < self._n:
            self.generator(left, right+1, one_result+")")
        else:
            self._total_result.append(one_result)
                


solution = Solution()
n = 3
print(solution.generateParenthesis(n))


        