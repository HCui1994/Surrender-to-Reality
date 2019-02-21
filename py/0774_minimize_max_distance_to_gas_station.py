"""
On a horizontal number line, we have gas stations at positions stations[0], stations[1], ..., stations[N-1], where N = stations.length.
Now, we add K more gas stations so that D, the maximum distance between adjacent gas stations, is minimized.
Return the smallest possible value of D.

Example:
Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
Output: 0.500000
Note:

1.  stations.length will be an integer in range [10, 2000].
2.  stations[i] will be an integer in range [0, 10^8].
3.  K will be an integer in range [1, 10^6].
4.  Answers within 10^-6 of the true value will be accepted as correct.
"""

class Solution:
    def min_max_gas_dist_minheap_wrong(self, stations, k):
        """
        greedy, 每次在相隔最远的两座加油站之间插入
        用什么数据结构来维护？最小堆.
        这是一个错误的解。为什么？
        注意！！！ 有可能原本相邻的两个 station 之间，插入了不止一个 额外的 station ！！！
        那么如何确定应该插入多少个 station ？
        """
        import heapq
        dist = []
        for idx in range(1, len(stations), +1):
            dist.append(float(stations[idx] - stations[idx - 1]))
        heapq._heapify_max(dist)
        print(dist)
        for _ in range(k):
            max_dist = heapq._heappop_max(dist)
            dist += [max_dist / 2, max_dist / 2]
            heapq._heapify_max(dist)
            print(dist)
        return dist[0]

    def min_max_gas_dist_brutal(self, stations, k):
        """
        Repeatedly add a gas station to the current largest interval, so that we add K of them total. 
        This greedy approach is correct because if we left it alone, then our answer never goes down from that point on.
        To find the largest current interval, we keep track of how many parts count[i] the ith (original) interval has become. 
        (For example, if we added 2 gas stations to it total, there will be 3 parts.) 
        The new largest interval on this section of road will be deltas[i] / count[i].
        """
        # 初始 station 数量
        N = len(stations)
        # 初始 相邻 station 间距
        deltas = [float(stations[i + 1] - stations[i]) for i in range(N - 1)]
        # 初始每个区间有多少个 station
        count = [1] * (N - 1)

        for _ in range(k):
            # 找到当前哪个区间中，station之间的间距最大
            best = 0
            for i, x in enumerate(deltas):
                if x / count[i] > deltas[best] / count[best]:
                    best = i
            # 往里面再插入一个 station
            count[best] += 1
        print(max(x / count[i] for i, x in enumerate(deltas)))

    def min_max_gas_dist_minheap(self, stations, k):
        """
        最小堆解正确解法
        """
        import heapq
        min_heap = [] #(-part_length, original_length, num_parts)
        for i in range(len(stations) - 1):
            curr, succ = stations[i], stations[i + 1]
            # 用间距的相反数（负值），由维护一个最大堆，变成维护一个最小堆
            min_heap.append((curr - succ, succ - curr, 1))
        heapq.heapify(min_heap)
        for _ in range(k):
            part_length, segment_length, num_parts = heapq.heappop(min_heap)
            num_parts += 1
            heapq.heappush(min_heap, (-(segment_length / float(num_parts)), segment_length, num_parts))
        print(-min_heap[0][0])
    
    def min_max_gas_dist_dp(self, stations, k):
        """
        子问题是什么？memo[i][k]: 表示向前 i 个区间中，插入 k 个额外 station 的结果
        """
        import numpy as np
        memo = [[stations[interval + 1] - stations[interval] for _ in range(k + 1)] for interval in range(len(stations) - 1)]
        # print(np.array(memo))
        for ik in range(k + 1):
            # 初始化，向第 0 区间中插入 0，1，2，3，...，k 个 station
            memo[0][ik] = (stations[1] - stations[0]) / (ik + 1)
        # print(np.array(memo))
        for interval in range(1, len(stations) - 1, +1):
            for ik in range(k + 1):
                memo[interval][ik] = min(max((stations[interval + 1] - stations[interval]) / float(interval + 1), memo[interval - 1][ik - ik_in_curr_inter]) for ik_in_curr_inter in range(ik+1))
                # for ik_in_curr_inter in range(ik + 1):
                #     max_part_length = max((stations[interval + 1] - stations[interval]) / (ik_in_curr_inter + 1), memo[interval - 1][ik - ik_in_curr_inter])
                #     memo[interval][ik] = min(max_part_length, memo[interval][ik - ])
        print(np.array(memo))
        print(memo[-1][k])

    def min_max_gas_dist_dp_2(self, stations, K):
        import numpy as np
        N = len(stations)
        deltas = [stations[i+1] - stations[i] for i in range(N-1)]
        dp = [[0.0] * (K+1) for _ in range(N-1)]
        #dp[i][j] = answer for deltas[:i+1] when adding j gas stations
        for i in range(K+1):
            dp[0][i] = deltas[0] / float(i + 1)

        for p in range(1, N-1):
            for k in range(K+1):
                dp[p][k] = min(max(deltas[p] / float(x+1), dp[p-1][k-x]) for x in range(k+1))
        print(np.array(dp))
        return dp[-1][K]

    def min_max_gas_dist_binary_search(self, stations, k):
        

    def test(self):
        stations = [1,7,11,19,20,36,56,77,90]
        k = 9
        self.min_max_gas_dist_brutal(stations, k)
        self.min_max_gas_dist_minheap(stations, k)
        self.min_max_gas_dist_dp(stations, k)


soln = Solution()
soln.test()