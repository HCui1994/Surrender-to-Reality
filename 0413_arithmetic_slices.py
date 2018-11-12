"""
A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.

看起来有点类似于 0647 Palindromic Substring，但其实完全不一样
"""

class Solution:
    def num_of_arith_slices(self, A):
        """ actually brute force, TLE ??!!"""
        if len(A) < 3:
            return 0
        memo = [[False for _ in A] for _ in A]
        length = 3
        for i in range(len(A)):
            j = i + length - 1
            if j >= len(A):
                break
            if A[j] - A[j - 1] == A[j - 1] - A[i]:
                memo[i][j] = True
        for length in range(4, len(A) + 1, +1):
            print(length)
            for i in range(len(A) - 1):
                j = i + length - 1
                print(i, j)
                if j >= len(A):
                    break
                if memo[i][j - 1] and A[j] - A[j - 1] == A[j - 1] - A[j - 2]:
                    memo[i][j] = True
        count = 0
        for row in memo:
            count += sum(row)
        return count
    
    def num_of_arith_slices_dp(self, A):
        """
        先不考虑至少长度为 3 的要求
        如果一个序列 A 是arithmetic，长度为 l ，那么在后面添加一个数 a 成为 A'，并且使得 A'依然是 arithmetic
        以 a 结尾的 arithmetic 有 l+1 个

        memo[i] 表示 以 A[i] 结尾的 arith 有多少个
        """
        if len(A) < 3:
            return 0
        memo = [0 for _ in A]
        for idx in range(2, len(A), +1):
            if A[idx] - A[idx - 1] == A[idx - 1] - A[idx - 2]:
                memo[idx] = memo[idx - 1] + 1
            else:
                memo[idx] = 0
        return sum(memo)

    def test(self):
        A = [1, 2, 3, 4, 6, 7, 8, 9]
        ans = self.num_of_arith_slices_dp(A)
        print(ans)
    

soln = Solution()
soln.test()