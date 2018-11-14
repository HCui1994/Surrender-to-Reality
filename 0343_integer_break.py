"""
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.
"""

class Solution:
    def integer_break(self, n):
        """
        参考 2_keys_keyboard 和 4_keys_keyboard
        将 n 看作 i 个数的和，memo[n] 即是整数 n 对应的结果（最大product）
        n = Sum(n_1, n_2, ..., n_i)
        product_n = max_i(product_(n-i) * (n-i))
        product_(n-i) 即是子问题的解 
        """
        memo = [0 for _ in range(n + 1)]
        memo[2], memo[3] = 1, 2
        for i in range(4, n + 1, +1):
            for j in range(2, i // 2 + 1, +1):
                # j 只需要遍历到 i 的一半即可
                # 如果只拆分一次，必然是 i // 2 处拆分
                # 如果拆分多次，每个 j 必然小于 i // 2
                # 前一个 j 算出的结果
                res_wrt_perv_j = memo[i]
                # 当前 j, i - j 不拆分，即 整数 i 只拆分一次
                not_break_i_j = (i - j) * j # 注意！ 这一点非常容易忽略，导致结果错误
                # 当前 j, i - j 拆分，即整数 i 拆分多次
                break_i_j = memo[i - j] * j
                memo[i] = max(res_wrt_perv_j, not_break_i_j, break_i_j)
        print(memo)

    def test(self):
        n = 10
        self.integer_break(n)


soln = Solution()
soln.test()