"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
"""
import numpy as np


class Solution(object):
    def is_interleave_dp(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        if not s1:
            return True if s2 == s3 else False
        if not s2:
            return True if s1 == s3 else False

        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        dp[0][0] = True
        # 初始化
        # 当 s2 是空串时
        for s1_len in range(1, len(s1) + 1):
            if s1[:s1_len] == s3[:s1_len]:
                dp[s1_len][0] = True
            else:
                break
        for s2_len in range(1, len(s2) + 1):
            if s2[:s2_len] == s3[:s2_len]:
                dp[0][s2_len] = True
            else:
                break
        for s1_len in range(1, len(s1) + 1):
            for s2_len in range(1, len(s2) + 1):
                s3_len = s1_len + s2_len
                # 如果 s3 的结尾与 s1 s2 结尾均不相同，则不能穿插构成
                if s3[s3_len - 1] != s2[s2_len - 1] and s3[s3_len - 1] != s1[s1_len - 1]:
                    dp[s1_len][s2_len] = False
                    continue
                # 如果 s3 的结尾与 s2 结尾相同，与 s1 结尾不相同
                if s3[s3_len - 1] == s2[s2_len - 1] and s3[s3_len - 1] != s1[s1_len - 1]:
                    dp[s1_len][s2_len] = dp[s1_len][s2_len - 1]
                    continue
                if s3[s3_len - 1] != s2[s2_len - 1] and s3[s3_len - 1] == s1[s1_len - 1]:
                    dp[s1_len][s2_len] = dp[s1_len - 1][s2_len]
                    continue
                if s3[s3_len - 1] == s2[s2_len - 1] and s3[s3_len - 1] == s1[s1_len - 1]:
                    dp[s1_len][s2_len] = dp[s1_len][s2_len -
                                                    1] or dp[s1_len - 1][s2_len]
        print(np.array(dp))
        return dp[-1][-1]

    def is_interleaving_recursive_memoize(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        if not s1:
            return True if s2 == s3 else False
        if not s2:
            return True if s1 == s3 else False
        self.memo = {}
        print(self.dfs(s1, s2, s3))

    def dfs(self, s1, s2, s3):
        print(s1, s2, s3)
        if not s1 and not s2 and not s3:
            return True
        if not s1:
            return True if s2 == s3 else False
        if not s2:
            return True if s1 == s3 else False
        if (s1, s2) in self.memo:
            print("shit")
            return self.memo[s1, s2]
        if s1[0] != s3[0] and s2[0] != s3[0]:
            self.memo[s1, s2] = False
        elif s1[0] == s3[0] and s2[0] != s3[0]:
            self.memo[s1, s2] = self.dfs(s1[1:], s2, s3[1:])
        elif s1[0] != s3[0] and s2[0] == s3[0]:
            self.memo[s1, s2] = self.dfs(s1, s2[1:], s3[1:])
        elif s1[0] == s3[0] and s2[0] == s3[0]:
            self.memo[s1, s2] = self.dfs(s1, s2[1:], s3[1:]) or self.dfs(s1[1:], s2, s3[1:])
        return self.memo[s1, s2]

        return
        
        
        

    def test(self):
        s1 = "aaaaaaaaaa"
        s2 = "aaaaaaaaba"
        s3 = "aaaaaaaaaaaabaaaaaaa"
        self.is_interleaving_recursive_memoize(s1, s2, s3)


Solution().test()
