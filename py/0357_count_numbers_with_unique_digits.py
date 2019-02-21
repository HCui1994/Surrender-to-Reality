"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10^n.

Example:

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99
"""

class Solution:
    def __init__(self):
        self._fact_memo = {}

    def count_number_with_unique_digits_dp(self, n):
        """
        dynamic programming and memoization
        最高位 9 个选项
        次高位 8 个
        再次 7 个
        再再次 6 个
        最多十位数，十位以上结果不在变 pigeon hole
        """
        if not n:
            return 1
        if n == 1:
            return 10
        memo = [None for i in range(min(n, 10) + 1)]
        memo[0], memo[1] = 1, 10
        for i in range(2, min(n, 10) + 1, +1):
            memo[i] = 9 * self._factorial(9) / self._factorial(9 - i + 1) + memo[i - 1]
        # print(memo)
        return int(memo[-1])
        
    def _factorial(self, x):
        if x in self._fact_memo.keys():
            return self._fact_memo[x]
        if x < 2:
            return 1
        else:
            self._fact_memo[x] = x * self._factorial(x - 1)
            return self._fact_memo[x]
    
    def test(self):
        x = 2
        ans = self.count_number_with_unique_digits(x)
        print(ans)


soln = Solution()
soln.test()
        