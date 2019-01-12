
class Solution(object):
    def isMatch(self, s, p):
        len_s = len(s)
        len_p = len(p)
        # initialize
        dp = [[False for i in range(len_p+1)] for j in range(len_s+1)]
        dp[0][0] = True
        # initialize dp[0][j]
        for j in range(1, len_p):
            if p[j] == '*':
                dp[0][j+1] = dp[0][j-1]
        for i in range(1, len_s+1):
            for j in range(1, len_p+1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = (dp[i-1][j-2] and (p[j-2] == s[i-1] or p[j-2] == '.')) or dp[i][j-2] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
        return dp[len_s][len_p]


    def test(self):
        s = "mississippi"
        p = "mis*is*p*."
        print(self.isMatch(s, p))


Solution().test()
