class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        memo = [None for _ in range(num + 1)]
        memo[:2] = [0, 1]
        for n in range(2, num + 1):
            if n % 2 == 0:  # 偶数相当于发生了一次向左位移，末尾补0，故1的数目不变
                memo[n] = memo[n // 2]
            else:           # 奇数相当于向左位移，末尾补1，故1的数目加一
                memo[n] = memo[n // 2] + 1
        return memo


soln = Solution()
num = 5
print(soln.countBits(num))


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

