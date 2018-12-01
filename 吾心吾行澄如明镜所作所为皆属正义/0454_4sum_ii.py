"""
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. 
All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:
Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
Output:
2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""

class Solution:
    # def four_sum_count_recursion_with_memoization(self, a, b, c, d):
    #     """
    #     recursion with memoization
    #     首先，肯定要遍历到所有的组合：recursive是一个好方法
    #     其次，如何降低计算量？
    #     """
    #     pass

    # def _recursion_with_memoization(self, a, b, c, d, ai, bi, ci, di, memo):
    #     if (ai, bi, ci, di) in memo.keys():
    #         return memo[(ai, bi, ci, di)]
        
    def four_sum_count(self, a, b, c, d):
        """
        想的太复杂了。回忆一下最简单的 two sum
        """
        # import collections
        # if not a:
            # return 0
        a_plus_b = collections.Counter(ai + bi for ai in a for bi in b)
        c_plus_d = collections.Counter(ci + di for ci in c for di in d)
        return sum([a_plus_b[-ci - di] for ci in c for di in d])

    def test(self):
        a = [ ]
        b = []
        c = []
        d = []
        print(self.four_sum_count(a, b, c, d))


Solution().test()