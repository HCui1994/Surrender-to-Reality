class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        memo = [0 for _ in range(num + 1)]
        memo[1] = 1
        for n in range(2, num + 1):
            if n % 2 == 0:
                memo[n] = memo[n // 2]
            else:
                memo[n] = memo[n // 2] + 1
        return memo


soln = Solution()
num = 5
soln.countBits(num)


"""
0       0
1       1
2       10
3       11
4       100
5       101
6       110
7       111
8       1000
9       1001
"""