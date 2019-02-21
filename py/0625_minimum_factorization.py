"""
Given a positive integer a, find the smallest positive integer b whose multiplication of each digit equals to a.
If there is no answer or the answer is not fit in 32-bit signed integer, then return 0.

Example 1
Input:
48 
Output:
68

Example 2
Input:
15
Output:
35
"""

class Solution:
    def smallest_fatorization_greedy(self, num):
        """
        贪心，每次找到最大的因子，放在最高位
        """
        if num < 10:
            return num
        res = 0
        high = 1
        while num > 1:
            valid_flag = False
            for factor in range(9, 1, -1):
                if num % factor == 0:
                    num //= factor
                    res += factor * high
                    high *= 10
                    valid_flag = True
                    break
            if not valid_flag:
                return 0
        if res >= 2 ** 31:
            return 0
        else:
            return res

    def smallest_factorization_recursive(self, num):
        res = ""
        if self._recursive(self, num, res):
            res = int(res)
            if res < 2 ** 31:
                return res
        return 0
    
    def _recursive(self, num, res):
        valid_flag = False
        for i in range(9, 1, -1):
            if num % factor == 0:
                res = str(factor) + res
                valid_flag = True
                break
        if valid_flag:
            return self._dfs(num // factor, res)
        else:
            return False

    def test(self):
        print(self.smallest_fatorization_greedy(15))


Solution().test()