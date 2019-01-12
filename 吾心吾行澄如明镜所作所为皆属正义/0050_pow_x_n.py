"""
Implement pow(x, n)

Example 1:
Input: 2.00000, 10
Output: 1024.00000

Example 2:
Input: 2.10000, 3
Output: 9.26100

Example 3:
Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Note:
-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""

class Solution(object):
    def trivial_pow(self, x, n):
        if n == 0:
            return 1
        sign = True if n > 0 else False
        ans = 1
        for _ in range(abs(n)):
            ans *= x
        return ans if sign else 1 / ans

    def binary_pow(self, x, n):
        if n == 0:
            return 1
        if n > 0:
            return self.binary_pow_helper(x, abs(n))
        else:
            return 1 / self.binary_pow_helper(x, abs(n))

    def binary_pow_helper(self, x, n):
        if n == 1:
            return x
        if n % 2:
            return self.binary_pow_helper(x, n // 2) ** 2 * x
        else:
            return self.binary_pow_helper(x, n // 2) ** 2

    def fast_pow(self, x, n):
        if n == 0:
            return 1
        self.fast_pow_memo = {}
        sign = True if n > 0 else False
        n = abs(n)
        ans = 1
        while n > 0:
            if n % 2:
                ans *= x
            n //= 2
            try:
                x **= 2
            except OverflowError:
                return float("inf") if sign else 0
        return ans if sign else 1 / ans
    
    def test(self):
        x, n = 2.00000, -2147483648
        print(self.fast_pow(x, n))


Solution().test()