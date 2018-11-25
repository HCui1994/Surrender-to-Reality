"""
Imagine you have a special keyboard with the following keys:

Key 1: (A): Print one 'A' on screen.

Key 2: (Ctrl-A): Select the whole screen.

Key 3: (Ctrl-C): Copy selection to buffer.

Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

Now, you can only press the keyboard for N times (with the above four keys), find out the maximum numbers of 'A' you can print on screen.
"""

class Solution:
    def four_keys_keyboard_dp(self, N):
        """
        全选复制粘贴共三次操作
        三连击A可以得到三个A
        长度为 x「scpp*」的连续操作，可以将之前的串长度乘以 x - 1
        """
        if N <= 6:
            return N
        memo = [0 for i in range(N + 1)]
        for i in range(1, 7, +1):
            memo[i] = i
        for i in range(7, N + 1, +1):
            # 令 最后一组操作序列 scpp* 长度为 j，j in [3, i - 3]
            # scpp*长度至少为3，至多为当前操作序列长度减3，因为初始三个操作必然是 单击 A
            for j in range(3, i - 3 + 1, +1):
                memo[i] = max(memo[i - j] * (j - 1), memo[i])
        return memo[-1]


        

    def test(self):
        N = 10
        self.four_keys_keyboard_dp(N)


soln = Solution()
soln.test()
