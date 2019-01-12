"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:
1.  s could be empty and contains only lowercase letters a-z.
2.  p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".

Example 5:
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""


class Solution(object):

    def is_match_nfa(self, string, pattern):
        """
        1.  p的长度为0，那么s也必须为0，否则不匹配。
        2.  p的长度为1，那么s的长度也必须为1，而且字母必须匹配。
        3.  p的长度大于等于2：
            3.1 p的第二位是*，比如“a*”或者“.*”：
                3.1.1   一种是match一个或者多个，比如“a*” match “a”，“aa”或者“aaaaa”。".*" match "abc"
                3.1.2   一种match“”空字符串。
                用一个while循环把match多个消掉成match“”空字符串。
            3.2 p的第二位不是*。
                那么检查p的第一位和s的第一位是不是match，然后递归match p的第二位开始和s的第二位开始。
                如果他们的第一位都不match，直接false。
        """
        self.string, self.pattern = string, pattern
        self.p_len, self.s_len = len(pattern), len(string)
        # return self.nfa(string, pattern)
        return self.fast_nfa(0, 0)

    def match(self, string, pattern):
        return string[0] == pattern[0] or pattern[0] == '.'

    def nfa(self, string, pattern):
        print(string, pattern)
        if not pattern:
            # case1: 剩余 pattern 长度为 0
            return not string
        elif len(pattern) == 1:
            # case2: pattern 剩余长度等于 1
            return len(string) == 1 and self.match(string, pattern)
        else:
            # case2: pattern 剩余长度大于等于 2
            if pattern[1] == '*':
                while string and self.match(string, pattern):
                    if self.nfa(string, pattern[2:]):
                        return True
                    string = string[1:]
                return self.nfa(string, pattern[2:]) # 非常容易忽略的一点，
            else:
                if string and self.match(string, pattern): # 剩余pattern，但string已全部匹配，返回false，非常容易忽略
                    return self.nfa(string[1:], pattern[1:])
                else:
                    return False

    def fast_match(self, s, p):
        return s == p or p == '.'

    def fast_nfa(self, s_idx, p_idx):
        """
        传入引用与指针，加速
        为什么反而更慢了？？？？
        """
        print(self.string[s_idx:], self.pattern[p_idx:])
        if p_idx == self.p_len:
            return s_idx == self.s_len
        elif p_idx == self.p_len - 1:
            return s_idx == self.s_len - 1 and self.fast_match(self.string[s_idx], self.pattern[p_idx])
        else:
            if self.pattern[p_idx + 1] == '*':
                while self.string[s_idx:] and self.fast_match(self.string[s_idx], self.pattern[p_idx]):
                    if self.fast_nfa(s_idx, p_idx + 2):
                        return True
                    s_idx += 1
                return self.fast_nfa(s_idx, p_idx + 2)
            else:
                if self.string[s_idx:] and self.fast_match(self.string[s_idx], self.pattern[p_idx]):
                    return self.fast_nfa(s_idx + 1, p_idx + 1)
                else:
                    return False


    def is_match_dp(self, string, pattern):
        """
        dp[i][j] 代表 string[:i] 和 pattern[:j] 能否匹配
        类似于 LCS？
<<<<<<< HEAD
        
        初始化：
        case1：string 与 pattern 均为空串时，显然匹配 => dp[0][0] = True
        case2：string 非空而 pattern 为空串时，显然不匹配 => dp[i][0] = False, where i > 0
        case3：string 为空串而 pattern 非空时：
            case3.1：pattern 仅有一位，不论 pattern 为何，军无法匹配 => dp[0][1] = False
            case3.2：pattern 有两位：
                case3.2.1：pattern = "**"，是无效的模式，dp[0][2] = False
                case3.2.2：pattern = "aa" or pattern = ".a" or pattern =  ".." => dp[0][2] = False
                case3.2.3：pattern = "a*" or pattern = ".*" => dp[0][2] = True
            case3.3：pattern 有大于两位，无法与空 string 匹配 => dp[0][j] = False, j > 2
        初始化完成

        转移方程：
        case1：若 string[i] = pattern[j] or pattern[j] = '.'，则在当前位上模式与文本相匹配，则 dp[i][j] 的状态取决于模式与文本前一位的状态，dp[i - 1][j - 1]
        case2：当前位不匹配
            case2.1：pattern[j] = '*'：
                case2.1.1：pattern[j - 1] = '*'：连续的两个星号，是不合法的模式，直接返回false
                case2.1.2：pattern[j - 1] = string[i]：模式 * 前一位与文本的当前位匹配，相当于模式中的 "a*" 匹配了文本中的 1 个字符，即当前字符 => dp[i][j] = dp[i][j - 1]
                case2.1.3：pattern[j - 1] != string[i]：模式 * 前一位与文本的当前位不匹配，相当于模式中的 "a*" 匹配了文本中的 0 个字符 => dp[i][j] = dp[i][j - 2]
            case2.2：当前模式位不是 *，且无法与当前文本为匹配 => dp[i][j] = false
        """
    def match(self, s, p):
        return s == p or p == '.'
    
    def is_match_dp(self, s, p):
        if s and not p:
            return False
        s_len, p_len = len(s), len(p)
        dp = [[None for _ in range(p_len + 1)] for _ in range(s_len + 1)]
        # init
        dp[0][0] = True
        for i in range(s_len):
            dpi = i + 1
            dp[dpi][0] = False # empty pattern cannot match non-empty string
        for j in range(p_len):
            dpj = j + 1
            for j in range(1, p_len):
                if p[j] == '*':
                    dp[0][dpj] = dp[0][dpj - 2]
        # transition function
        for i in range(s_len):
            dpi = i + 1
            for j in range(p_len):
                dpj = j + 1
                if self.match(s[i], p[j]):
                    dp[dpi][dpj] = dp[dpi - 1][dpj - 1]
                elif p[j] == '*' and not self.match(s[i], p[j - 1]):
                    # meets *, previous pattern symbol cannot match current string symbol <=> "a*" match 0 symbol
                    dp[dpi][dpj] = dp[dpi][dpj - 2]
                elif p[j] == '*' and self.match(s[i], p[j - 1]):
                    # meets *, previous pattern symbol matches current string symbol <=> "a*" matches at least 1 symbol
                    match_one = dp[dpi - 1][dpj - 2]
                    match_more_than_one = dp[dpi - 1][dpj]
                    dp[dpi][dpj] = match_one or match_more_than_one
                else:
                    dp[dpi][dpj] = False
        import numpy as np
        print(np.array(dp))
        return dp[-1][-1]
=======
        分析：
        若 string[i] == pattern[j] or pattern[j] == '.'，则 dp[i][j] = dp[i - 1][j - 1]
        若 pattern[j] == '*'
            若 string[i] == pattern[j - 1]，则 dp[i][j] = dp[i - 1][j - 1]
        """
        len_string, len_pattern = len(string), len(pattern)
        dp = [[False for _ in range(len_pattern + 1)] for _ in range(len_string + 1)]
        for i in range(len_string):
            for j in range(len_pattern):
>>>>>>> d2e6e43e2a641216a22d80b23c5632e6e25603ff

    def match_dp(self, s, p):
        return s == p or p == '.'

    def test(self):
        s = "mississippi"
        p = "mis*is*p*."
        print(self.is_match_dp(s, p))


Solution().test()
