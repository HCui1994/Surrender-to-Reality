class Solution:
    def __init__(self):
        self._factorial_memo = {}

    def climbStairs(self, n):
        """factorial memoization solution"""
        sum = 0
        for i in range(n // 2 + 1):
            sum += self._choose_m_n(n - i, i)
        return sum

    def _choose_m_n(self, m, n):
        return self._factorial(m) / self._factorial(m - n) / self._factorial(n)

    def _factorial(self, n):
        if n in self._factorial_memo:
            return self._factorial_memo[n]
        elif n == 0:
            return 1
        else:
            x = self._factorial(n - 1) * n
            self._factorial_memo[n] = x
            return x


    def climb_stairs_dp(self, n):
        """dp solution, very fast... actually fibonacci"""
        if not n:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp_memo = [0 for _ in range(n)]
        dp_memo[0], dp_memo[1] = 1, 2
        for i in range(2, n, +1):
            one_step = dp_memo[i - 1]
            two_step = dp_memo[i - 2]
            dp_memo[i] = one_step + two_step
        return dp_memo[-1]





soln = Solution()
print(soln.climb_stairs_dp(3))