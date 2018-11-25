class Solution(object):
    def isMatch(self, text, pattern):
        memo = {}

        def dp(text_idx, pattern_idx):
            print(memo)
            if (text_idx, pattern_idx) not in memo: # 还没有匹配过text[text_idx] 和 pattern[pattern_idx]
                if pattern_idx == len(pattern):     # 已经消耗完所有的 pattern
                    ans = text_idx == len(text)     # 并且也消耗完了所有的 text，则 ans == True
                else:
                    # first_match = 未消耗完所有text，且pattern可以匹配 （未遇到星号）
                    first_match = text_idx < len(text) and pattern[pattern_idx] in (text[text_idx], '.')
                    # 如果遇到了星号
                    if pattern_idx + 1 < len(pattern) and pattern[pattern_idx + 1] == '*':
                        ans = dp(text_idx, pattern_idx + 2) or first_match and dp(text_idx + 1, pattern_idx)
                    else:
                        ans = first_match and dp(text_idx+1, pattern_idx+1)

                memo[text_idx, pattern_idx] = ans

            return memo[text_idx, pattern_idx]

        return dp(0, 0)





class Solution2(object):
    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
        print(dp)
        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                # first match: 当前位置上，没有到文本末尾，且j位模式等于i位文本，或 ‘.’
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                # 如果j+1位模式不是末尾，且j+1位模式是 ’*‘
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]




text = "aaab"
pattern = "a*ab"
soln = Solution2()
print(soln.isMatch(text, pattern))