"""
Your music player contains N different songs and she wants to listen to L (not necessarily different) songs during your trip.  

You create a playlist so that:
Every song is played at least once
A song can only be played again only if K other songs have been played
Return the number of possible playlists.  As the answer can be very large, return it modulo 10^9 + 7.

Example 1:

Input: N = 3, L = 3, K = 1
Output: 6
Explanation: There are 6 possible playlists. [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1].
Example 2:

Input: N = 2, L = 3, K = 0
Output: 6
Explanation: There are 6 possible playlists. [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], [1, 2, 2]
Example 3:

Input: N = 2, L = 3, K = 1
Output: 2
Explanation: There are 2 possible playlists. [1, 2, 1], [2, 1, 2]
 

Note:

0 <= K < N <= L <= 100
"""
import numpy as np
import collections


class Solution(object):
    def num_playlists(self, n, l, k):
        """
        输入 
            n：一共有 n 首不同的歌
            l：想听 l 首歌不同的歌
            k：两首相同的歌的最小间距
        动态规划 dp[i][j]：前 i 次，播放了 j 首不同的歌，有多少种播放列表

        每到一个新状态，有两种情况：
        1. 播放一首已经听过的歌
            前 i - 1 次播放了 j 首不同的歌，可以播放的已经播放过的歌曲数量 max(j - k, 0)
        2. 播放一首还没有听过的歌
            前 i - 1 次播放了 j - 1 首不同的歌，还剩 n - (j - 1) 首不同的歌曲未播放过
        """
        dp = [[0 for _ in range(n + 1)] for _ in range(l + 1)]
        # 没有曲库，也没有想听的歌
        dp[0][0] = 1
        MOD = 1000000007
        for i in range(1, l + 1):
            for j in range(1, n + 1):
                if j > i:
                    continue
                play_new_song = dp[i - 1][j - 1] * (n - (j - 1)) % MOD
                play_old_song = dp[i - 1][j] * max(j - k, 0) % MOD
                # print(play_new_song, play_old_song)
                dp[i][j] = (play_new_song + play_old_song) % MOD
                # print(np.array(dp))
        
        return dp[l][n]
                


    def test(self):
        N = 2
        L = 3
        K = 0
        print(self.num_playlists(N, L, K))


Solution().test()
