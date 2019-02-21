"""
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
"""
import numpy as np
class Solution:
    def longest_palindormic_sub_seq_dp(self, s):
        """
        dynamic programming，当确定了 序列 s[i:j] 的回文子序列长度时，
        若 s[i-1] == s[j]，则 s[i-1:j+1] 回文子序列长度 +2
        若 s[i-1] != s[j]，则 s[i-1:j+1] 回文子序列长度不变
        要注意串的长度是奇数还是偶数

        TLE, Python O(n^2)...
        Java can pass
        """
        str_length = len(s)
        memo = [[0 for j in range(str_length + 1)] for _ in range(str_length)]
        for i in range(str_length):
            memo[i][i + 1] = 1
        # for i in range(str_length - 1):
        #     if s[i] == s[i + 1]:
        #         memo[i][i + 2] = 2 
        # print(np.array(memo))
        # for length in range(2, str_length + 1):
        #     for i in range(str_length - 1):
        for length in range(2, str_length + 1):
            for i in range(str_length - length + 1):
                j = i + length
                # print(i, j)
                if j > str_length:
                    break
                if s[i] == s[j - 1]:
                    # 如果 s[i] == s[j - 1]，则 memo[i][j] 在 memo[i + 1][j - 1] 的基础上扩大 2 
                    memo[i][j] = memo[i + 1][j - 1] + 2
                else:
                    # 否则，就取 长度-1 的字串的解中，较大的
                    memo[i][j] = max(memo[i + 1][j], memo[i][j - 1])
        print(np.array(memo))
        return memo[0][str_length]

    def longest_palindromic_sub_seq_dp_mem_opt(self, s):
        str_length = len(s)
        memo = [1 for _ in range(str_length)]
        memo[0] = 0
        for length in range(2, str_length):
            for i in range(str_length - length + 1):
                j = i + length
                if s[i] == s[j - 1]:
                    memo[length] = memo[length - 2] + 2
                else:
                    memo[length] = max(memo[length], memo[length - 1])
        return memo[-1]
        

    def test(self):
        s = "aa"
        ans = self.longest_palindromic_sub_seq_dp_mem_opt(s)      
        print(ans)

        
soln = Solution()
soln.test()