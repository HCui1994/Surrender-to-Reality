"""
Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

Example 1:
Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
Note:
The n will be in the range [1, 1000].
"""
import math
class Solution:
    def min_steps_dp(self, n):
        """
        n       op              num of op           largest factor other than itself
        1       None            0                   None
        2       cp              2                   1
        3       cpp             3                   1
        4       cpcp            4 = 2+2             2
        5       cpppp           5                   1
        6       cppcp           5 = 3+2             3
        7       cpppppp         7                   1
        8       cpcpcp          6 = 4+2             4
        9       cppcpp          6                   3
        10      cppppcp         7 = 5+2             5
        11      cpppppppppp     11                  1
        12      cppcpcp         7 = 5+2             6
        因式分解
        """
        if n == 1:
            return 0
        if n <= 5:
            return n
        memo = [None for _ in range(n + 1)]
        memo[1], memo[2], memo[3] = 0, 2, 3
        for x in range(4, n + 1, +1):
            print(x)
            print(memo)
            prime_flag = True
            for factor in range(x // 2, 1, -1):
                # 寻找 x 的最大因子
                if x % factor == 0:
                    memo[x] = memo[x // factor] + factor
                    prime_flag = False
                    continue
            if prime_flag:
                memo[x] = x

        return memo[-1]

    def min_steps_math(self, n):
        """
        如何快速找到最大因子？
        """
    
    def test(self):
        n = 12
        self.minSteps(n)


soln = Solution()
soln.test()
