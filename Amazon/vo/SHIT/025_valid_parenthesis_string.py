import numpy as np

class Parenthesis(object):
    def is_valid(self, string):
        n = len(string)
        dp = [[False for _ in range(n)] for _ in range(n)]
        # init
        for i in range(n):
            if string[i] == '*':
                dp[i][i] = True
        for i in range(n - 1):
            if string[i] in "(*" and string[i + 1] in "*)":
                dp[i][i + 1] = True
        for l in range(3, n + 1):
            for i in range(n):
                j = i + l - 1
                if j >= n:
                    continue  
                if string[i] in '(*' and string[j] in "*)":
                    if dp[i + 1][j - 1]:
                        dp[i][j] = True
                        continue
                    for k in range(i, j + 1):
                        if dp[i][k] and dp[k + 1][j]:
                            dp[i][j] = True
                            break
        # print(np.array(dp))
        return dp[0][-1]


if __name__ == "__main__":
    p = Parenthesis()
    res = p.is_valid("(*)")
    print(res)
