"""
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
(ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?
"""

class Solution:
    def is_subsqeuence(self, s, t):
        """
        dynamic programming
        完全的 LCS 问题
        如果LCS 长度等于 短字符串的长度，return true

        TLE! 
        """
        if not s:
            return True
        # memo[i+1][j+1j 记录了 s[:i+1], t[:j+1] 的 LCS 长度
        memo = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    # s[i] == t[j] 则 当前 LCS 是 s[:i], t[:j]的 LCS 的扩增
                    memo[i + 1][j + 1] = memo[i][j] + 1
                else:
                    # s[i] != t[j]，则 当前 LCS 是s[:i],t[:j+1]的 LCS 和 s[:i+1],t[:j]的LCS 中 较大的一个
                    memo[i + 1][j + 1] = max(memo[i][j + 1], memo[i + 1][j])
        print(memo[-1][-1])
        if memo[-1][-1] == len(s):
            return True
        else:
            return False


    def is_subsequence_simple(self, s, t):
        """
        不要把问题想得太复杂
        不需要求子序列长度，只要判断是否是子序列，不需要太多信心
        熵太大，系统复杂，时间自然就长了
        """
        if not s:
            return True
        j = 0
        for x in t:
            if s[j] == x:
                j += 1
            if j == len(s):
                return True
        return False

    def test(self):
        # s = "abc"
        # t = "ahbgdc"

        s = "axc"
        t = "ahbgdc"
        ans = self.is_subsequence_simple(s, t)
        print(ans)


soln = Solution()
soln.test()

