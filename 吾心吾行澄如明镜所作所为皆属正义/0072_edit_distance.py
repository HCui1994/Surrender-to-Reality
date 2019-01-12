"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
You have the following 3 operations permitted on a word:
Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""

class Solution(object):
    def min_distance_dp(self, word1, word2):
        """
        考虑动态规划，dp[i][j] 表示 word1[:i]，word2[:j] 匹配需要的改动数
        初始化：
        word1，word2 均为空时，不需要任何改动
        word1 为空，word2 不为空时，需要的改动数即 word2 的长度
        word1 不为空，word2 为空时，需要的改动数即 word1 的长度

        转移方程：
        case1：word[i] = word[j]，当前位上的字母相等，dp[i][j] 取决于 dp[i - 1][j - 1]
        case2：word[i] != word[j], 取决于 dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1] 中的最小值，再加上当前位的一次 edit
        """
        import numpy as np
        word1_len, word2_len = len(word1), len(word2)
        dp = [[None for _ in range(word2_len + 1)] for _ in range(word1_len + 1)]
        # init
        dp[0][0] = 0 # word1 word2 均为空串时，不需要任何改动
        for i in range(word1_len):
            dpi = i + 1
            dp[dpi][0] = i + 1
        for j in range(word2_len):
            dpj = j + 1
            dp[0][dpj] = j + 1
        for i in range(word1_len):
            dpi = i + 1
            for j in range(word2_len):
                dpj = j + 1
                dp[dpi][dpj] = dp[dpi - 1][dpj - 1] if word1[i] == word2[j] else min(dp[dpi - 1][dpj - 1], dp[dpi][dpj - 1], dp[dpi - 1][dpj]) + 1
        print(np.array(dp))
        return dp[-1][-1]

    def min_distance_bfs(self, word1, word2):
        

    def test(self):
        word1 = "horse"
        word2 = "ros"
        self.min_distance(word1, word2)


Solution().test()