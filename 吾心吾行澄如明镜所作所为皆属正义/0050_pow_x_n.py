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

Note:
1.  -100.0 < x < 100.0
2.  n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""


class Solution(object):
    def fast_pow(self, x, n):
        if n == 0:
            return 1
        sign = 1 if n > 0 else -1
        n = abs(n)
        sub_n_list = []
        sum_sub_n, sub_n = 0, 1
        while sum_sub_n < n:
            sub_n_list.append(sub_n)
            sum_sub_n += sub_n
            sub_n *= 2
        if sum_sub_n > n:
            sum_sub_n -= sub_n_list.pop()
            sub_n_list += [sub_n_list[-1], sum_sub_n - sub_n_list[-1]]
        print(sub_n_list)
        
        

    def test(self):
        x = 2
        n = 15
        self.fast_pow(x, n)


Solution().test()
