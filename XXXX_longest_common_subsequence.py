"""
1. 子序列(subsequence)： 一个特定序列的子序列就是将给定序列中零个或多个元素去掉后得到的结果(不改变元素间相对次序)。
    例如序列 <A,B,C,B,D,A,B> <A,B,C,B,D,A,B> 的子序列有：
    <A,B> <A,B>、<B,C,A> <B,C,A>、<A,B,C,D,A> <A,B,C,D,A>等。 
2. 公共子序列(common subsequence)：给定序列X和Y，序列Z是X的子序列，也是Y的子序列，则Z是X和Y的公共子序列。
    例如 X = <A,B,C,B,D,A,B>    X = <A,B,C,B,D,A,B>， Y = <B,D,C,A,B,A>     Y = <B,D,C,A,B,A>，
    那么序列Z=<B,C,A>Z=<B,C,A>为X和Y的公共子序列，其长度为3。但ZZ不是XX和YY的最长公共子序列，
    而序列<B,C,B,A><B,C,B,A>和<B,D,A,B><B,D,A,B>也均为XX和YY的最长公共子序列，长度为4，而XX和YY不存在长度大于等于5的公共子序列。 
3.最长公共子序列问题(LCS:longest-common-subsequence problem)：
    In the longest-common-subsequence problem, we are given two sequences 
    X=<x1,x2,...,xm>X=<x1,x2,...,xm> and Y=<y1,y2,...,yn>Y=<y1,y2,...,yn> 
    and wish to find a (not “the”) maximum-length common subsequence of XX and YY . 
    This section shows how to efficiently solve the LCS problem using dynamic programming.
"""
import numpy as np
class Solution:
    def longest_common_subsequence_brutal(self, x, y):
        """
        1. 枚举序列X里的每一个子序列 xi；
        2. 检查子序列 xi 是否也是 Y 序列里的子序列；
        3. 在每一步记录当前找到的子序列里面的最长的子序列。
            T(n) in O(n * 2 ^ m)
        """
        pass

    def longest_common_subsequence(self, x, y):
        if not x or not y:
            return 0
        memo = [[0 for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]
        for i in range(len(x)):
            memo_i = i + 1
            for j in range(len(y)):
                memo_j = j + 1

                if x[i] == y[j]:
                    # 如果 x[i] == y[j] == z[k] 
                    # 则 z[:k] 是 x[:i], y[:j] 的 LCS
                    memo[memo_i][memo_j] = memo[memo_i - 1][memo_j - 1] + 1
                else:
                    # 如果 x[i] != y[j]，即 z[k] != x[i], z[k] != y[j]
                    # 则 z[:k] 是 x[:i], y[:j - 1] 的 LCS；或 x[:i - 1]，y[:j] 的 LCS
                    memo[memo_i][memo_j] = max(memo[memo_i - 1][memo_j], memo[memo_i][memo_j - 1])
        print(np.array(memo))


    def test(self):
        x = "qwertyuiop"
        y = "q e t u o"
        self.longest_common_subsequence(x, y)
    

soln = Solution()
soln.test()

