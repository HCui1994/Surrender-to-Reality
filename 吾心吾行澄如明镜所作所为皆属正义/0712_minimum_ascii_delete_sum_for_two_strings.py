"""
Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
Example 2:
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
Note:

0 < s1.length, s2.length <= 1000.
All elements of each string will have an ASCII value in [97, 122].
"""

class Solution:
    def minimum_delete_lcs(self, s1, s2):
        """ 
        LCS 变体
        用 LCS‘ 的 ascii value 代替长度
        """
        
        s1 = [ord(l) for l in s1]
        s2 = [ord(l) for l in s2]
        if not s1:
            return sum(s2)
        if not s2:
            return sum(s1)
        memo = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        for i in range(len(s1)):
            mi = i + 1
            for j in range(len(s2)):
                
                mj = j + 1
                if s1[i] == s2[j]:
                    # 如果发现相同字符
                    memo[mi][mj] = memo[mi - 1][mj - 1] + s1[i]
                else:
                    memo[mi][mj] = max(memo[mi][mj - 1], memo[mi - 1][mj])
        return sum(s1) - memo[-1][-1] + sum(s2) - memo[-1][-1]

    def test(self):
        s1 = "delete"
        s2 = "leet"
        ans = self.minimum_delete_lcs(s1, s2)
        print(ans)
            
soln = Solution()
soln.test()