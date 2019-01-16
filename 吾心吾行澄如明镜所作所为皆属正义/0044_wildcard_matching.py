"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:
Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:
Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:
Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""


class Solution(object):
    def wildcard_matching_recursion(self, string, pattern):
        """
        TLE
        """
        return self.nfa(string, pattern)

    def is_match(self, string, pattern):
        return string[0] == pattern[0] or pattern[0] == "?"

    def nfa(self, string, pattern):
        if not pattern and not string:
            return True
        if not pattern and string:
            return False
        if pattern and not string:
            for char in pattern:
                if char != '*':
                    return False
            return True
        if pattern[0] != '*':
            if self.is_match(string, pattern):
                return self.nfa(string[1:], pattern[1:])
            else:
                return False
        else:
            print("shit")
            for idx in range(len(string) + 1):
                print(string[idx:])
                if self.nfa(string[idx:], pattern[1:]):
                    return True
            return False

    def wildcard_matching_dp(self, string, pattern):
        """
        dp[i][j] 代表 string[0..i] pattern[0..j] 是否匹配
        初始化：
        string 和 pattern 均为空，匹配成功
        string 非空但 pattern 为空，匹配失败
        string 为空但 pattern 非空，仅当 pattern 全部为 * 匹配成功

        状态转移：考察 i，j
        case1：string[i], pattern[j] 可以匹配，则 dp[i][j] = dp[i - 1][j - 1]
        case2：
        """
        import numpy as np
        dp = [[None for _ in range(len(pattern) + 1)] for _ in range(len(string) + 1)]
        dp[0][0] = True 
        for i in range(len(string)):
            dpi = i + 1
            dp[dpi][0] = False
        nonempty_pattern_init = True
        for j in range(len(pattern)):
            dpj = j + 1
            if pattern[j] != '*':
                nonempty_pattern_init = False
            dp[0][dpj] = nonempty_pattern_init
        for i in range(len(string)):
            dpi = i + 1
            for j in range(len(pattern)):
                dpj = j + 1
                if pattern[j] != '*':
                    if self.is_match(string[i], pattern[j]):
                        dp[dpi][dpj] = dp[dpi - 1][dpj - 1]
                    else:
                        dp[dpi][dpj] = False
                else:
                    dp[dpi][dpj] = False
                    # dpi_idx = dpi
                    # while not dp[dpi][dpj] and dpi_idx >= 0:
                    #     dp[dpi][dpj] = dp[dpi][dpj] or dp[dpi_idx][dpj - 1]
                    #     dpi_idx -= 1
                    # 优化方法
                    dp[dpi][dpj] = dp[dpi - 1][dpj] or dp[dpi][dpj - 1]
        print(np.array(dp))
        return dp[-1][-1]
        
    

    def test(self):
        s = "adceb"
        p = "*a*b"
        # print(self.wildcard_matching(string, pattern))
        print(self.wildcard_matching_dp(s, p))

Solution().test()