"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution:
    def longest_palindrome_dp(self, s):
        """
        考虑 s[i:j] 的子串，如果其是回文串，用 memo[i][j] = len(s[i:j])，如果不是回文串，memo[i][j] = 0
        s[i:j] 的子问题：s[i+1: j-1] 是否为回文串？
        如果 s[i+1 : j-1] 是回文串（memo[i+1][j-1] != 0）且 s[i] == s[j - 1]，则 memo[i][j] = memo[i+1][j-1] + 2
        否则, memo[i+1][j-1] = 0
        """
        # 注意 edge case
        if len(s) < 2:
            return s
        str_len = len(s)
        memo = [[0 for _ in range(str_len + 1)] for _ in range(str_len)]
        for i in range(str_len):
            memo[i][i + 1] = 1
            # if i + 1 < str_len and s[i] == s[i + 1]:
            #     memo[i][i + 2] = 2
        max_len = 1
        # 注意 edge case
        max_coord = (0, 1)
        for length in range(2, str_len + 1, +1):
            for i in range(str_len - length + 1):
                j = i + length
                if s[i] == s[j - 1] and (memo[i + 1][j - 1] or i + 2 == j):
                    print(i, j)
                    memo[i][j] = memo[i + 1][j - 1] + 2
                    if memo[i][j] > max_len:
                        max_coord = (i, j)
        # print(memo)
        return s[max_coord[0] : max_coord[1]]

    def longest_palindrome_dp_2(self, s):
        """
        没有必要记录下来回文串的长度，只需要知道子问题是否为回文串
        """
        if len(s) < 2:
            return s
        str_len = len(s)
        memo = [[False for _ in range(str_len + 1)] for _ in range(str_len)]
        for i in range(str_len):
            memo[i][i + 1] = True
        max_len = 1
        max_coord = (0, 1)
        for length in range(2, str_len, +1):
            for i in range(str_len - length + 1):
                j = i + length
                if s[i] == s[j] and (memo[i + 1][j - 1] or i + 2 == j):
                    memo[i][j] = True
                    if length > max_len:
                        max_coord = (i, j)
        return s[max_coord[0] : max_coord[1]]

    def longest_palindrome_manacher(self, s):
        """
        马拉车

        1. 预处理，间隔添加哨兵字符，使得不论原字符串长度是奇数还是偶数，处理之后得到的字符串的长度都是奇数
        bob    -->    #b#o#b#
        noon   -->    #n#o#o#n# 

        2. 接下来我们还需要和处理后的字符串t等长的数组p，其中p[i]表示以t[i]字符为中心的回文子串的半径，若p[i] = 1，则该回文子串就是t[i]本身
        example：
        sentinal_t      # 1 # 2 # 2 # 1 # 2 # 2 #
        p               1 2 1 2 5 2 1 6 1 2 3 2 1
        以中间的 '1' 为中心的回文子串 "#2#2#1#2#2#" 的半径是6，而为添加井号的回文子串为 "22122"，长度是5，为半径减1
        所以只要找到了最大的半径，就知道最长的回文子串的长度
        但是只知道长度无法确定子串，还需要知道子串的起始位置。

        3. 为 t 数组添加新的哨兵
        sentinal_t      $ # 1 # 2 # 2 # 1 # 2 # 2 #
        p                 1 2 1 2 5 2 1 6 1 2 3 2 1
        以中间的 '1' 为中心的回文子串 "#2#2#1#2#2#" 的半径是6，位置为8
        起始位置为 (中间位置 - 半径) // 2

        4. 如何求解 p 数组？
        增两个辅助变量
        id：能延伸到最右端的位置的那个回文子串的中心点位置
        mx：回文串能延伸到的最右端的位置

        IF mx > i THEN
            p[i] = min( p[2 * id - i] , mx - i )
        ELSE    
            p[i] = 1

        ??????????
        """
        # preprocess, 不论原字符串长度是奇数还是偶数，处理之后得到的字符串的长度都是奇数
        sentinal_str = "#"
        for l in s:
            sentinal_str += l + "#"


    def test(self):
        s = "a"
        ans = self.longest_palindrome_dp_2(s)
        print(ans)


soln = Solution()
soln.test()