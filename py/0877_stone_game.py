"""
Alex and Lee play a game with piles of stones.  
There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].
The objective of the game is to end with the most stones. The total number of stones is odd, so there are no ties.
Alex and Lee take turns, with Alex starting first. Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  
This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

Example 1:

Input: [5,3,4,5]
Output: true
Explanation: 
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
 

Note:

1. 2 <= piles.length <= 500
2. piles.length is even.
3. 1 <= piles[i] <= 500
4. sum(piles) is odd.
"""

class Solution:
    def stone_game_dp(self, piles):
        """
        与 0468 predict the winner 完 全 一 致
        此问题的通用解，所以不是很快
        """
        num_piles = len(piles)
        if num_piles == 2:
            return True
        # memo[i][j] 代表 从 piles[i:j] 中取石子，Alex 能取到的最多石子数和  这一堆石子总数
        memo = [[[None, None] for _ in range(num_piles + 1)] for _ in range(num_piles)]
        # 初始化，只有一堆石子时，alex 最多能取到的石子数和总石子数
        for i in range(num_piles):
            memo[i][i + 1] = [piles[i], piles[i]]
        # 从长度为 2 的石子堆开始考虑
        for l in range(2, num_piles + 1, +1):
            # 注意长度的取值范围，l 最大可以取到 num_piles， l in range(2, num_piles + 1)
            for i in range(0, num_piles - 1, +1):
                # 注意 i 的范围，后续存在对下标 i+1 的访问，i 需要 in range(0, num_piles - 1)
                j = i + l
                if j > num_piles:
                    continue
                # 如果从 alex 从 piles[i:j] 的左侧取一堆石子，则 memo[i+1:j]表示 lee 可以去到的最多石子数 和 piles[i:j] 的总石子数
                # print(i, j)
                pick_from_left = piles[i] + memo[i + 1][j][1] - memo[i + 1][j][0]
                # 从右侧取 同理
                pick_from_right = piles[j - 1] + memo[i][j - 1][1] - memo[i][j - 1][0]
                # 找到 alex 能取到最大石子数
                memo[i][j][0] = max(pick_from_left, pick_from_right)
                # 算出 piles[i:j] 的总石子数
                memo[i][j][1] = piles[j - 1] + memo[i][j - 1][1]
        print(memo[0][num_piles])
        return memo[0][num_piles][1] // memo[0][num_piles][0] == 1

    def stone_game_special_soln(self, piles):
        """
        由于石子堆的总数是 偶数，假设有四个
        假设 四个数 a > b > c > d
        排列： a b c d
        alex: a     lee: b      alex: c     lee: d
        排列： a c b d
        alex: a     lee: c      alex: b     lee: d
        排列： a d c b
        alex: a     lee: b      alex: c     lee: d
        ...
        alex 总是会取到所有的偶数堆
        （或者所有的奇数堆）
        
        又因为总能分出胜负
        所以 先手总能获胜？
        直接 return true？？？！！！
        """
        return True

    def stone_game_dp_mem_opt(self, piles):
        """ 背包 ？？ """
        n = len(piles)
        # memo[i] 代表 从 i 开始的一堆石子，alex - lee 的差值
        memo = piles[:]
        for l in range(1, n):
            for i in range(n - l):
                memo[i] = max(piles[i] - memo[i + 1], piles[i + l] - memo[i])
        return memo[0] > 0
    
    def test(self):
        piles = [5,3,4,5]
        ans = self.stone_game(piles)
        print(ans)


soln = Solution()
soln.test()