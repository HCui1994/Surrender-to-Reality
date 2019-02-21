"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:
Input: [5,7]
Output: 4

Example 2:
Input: [0,1]
Output: 0
"""


class Solution:
    def range_bitwise_and(self, m, n):
        """
        找到 m n 高位连续全 1 的公共部分
        """
        INT_MAX = 2147483647
        print("m & mask\tn & mask \tmask")
        print(bin(m & INT_MAX),"\t\t", bin(n & INT_MAX), "\t\t", bin(INT_MAX))
        while (m & INT_MAX) != (n & INT_MAX):
            INT_MAX <<= 1
            print(bin(m & INT_MAX),"\t\t", bin(n & INT_MAX), "\t\t", bin(INT_MAX))
        print(m & INT_MAX)

    def test(self):
        m = 6
        n = 13
        self.range_bitwise_and(m, n)


soln = Solution()
soln.test()