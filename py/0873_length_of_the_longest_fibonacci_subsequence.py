"""
A sequence X_1, X_2, ..., X_n is fibonacci-like if:

n >= 3
X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
Given a strictly increasing array A of positive integers forming a sequence, find the length of the longest fibonacci-like subsequence of A.  
If one does not exist, return 0.

(Recall that a subsequence is derived from another sequence A by deleting any number of elements (including none) from A, 
without changing the order of the remaining elements.  
For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].)

Example 1:
Input: [1,2,3,4,5,6,7,8]
Output: 5
Explanation:
The longest subsequence that is fibonacci-like: [1,2,3,5,8].

Example 2:
Input: [1,3,7,11,12,14,18]
Output: 3
Explanation:
The longest subsequence that is fibonacci-like:
[1,11,12], [3,11,14] or [7,11,18].
"""


class Solution:
    def len_longest_fib_subseq(self, seq):
        """
        子问题是什么？
        memo[i] 表示 seq[:i] 的最长的 fib-like 子序列长度。如何计算？

        注意 memo 的意义
        """
        num_index = {}
        for idx, num in enumerate(seq):
            num_index[num] = idx
        # 考虑 fib-like seq 中相邻的两个数 
        # for example：假设 seq[i] + seq[j] = seq[k]，则 memo[j][k] = memo[i][j] + 1
        memo = [[2 for _ in seq] for _ in seq]
        max_len = 0
        for i in range(len(seq) - 2):
            for j in range(i + 1, len(seq) - 1):
                first = seq[i]
                second = seq[j]
                third = first + second
                if third in num_index.keys():
                    k = num_index[third]
                    memo[j][k] = memo[i][j] + 1
                    max_len = max(max_len, memo[j][k])
        # print(memo)
        return max_len

    def test(self):
        seq = [1,3]
        ans = self.len_longest_fib_subseq(seq)
        print(ans)


soln = Solution()
soln.test()