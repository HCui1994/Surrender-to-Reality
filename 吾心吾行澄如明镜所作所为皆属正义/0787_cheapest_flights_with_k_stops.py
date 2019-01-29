"""
There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, 
    your task is to find the cheapest price from src to dst with up to k stops. 
If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 

Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation: 

Note:
The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.
"""


class Solution:
    def build_graph(self, edges, n):
        graph = {x: set() for x in range(n)}
        for u, v, w in edges:
            graph[u].add((v, w))
        return graph

    def find_cheapest_price_dfs(self, n, flights, src, dst, k):
        """
        TLE
        """
        self.graph = self.build_graph(flights, n)
        self.prices = {x: float("inf") for x in range(n)}
        self.k = k
        self.finder(stop=src, total_price=0, nstops=0)
        # print(self.prices)
        return -1 if self.prices[dst] == float("inf") else self.prices[dst]

    def finder(self, stop, total_price, nstops):
        if nstops - 1 > self.k:
            return
        self.prices[stop] = min(self.prices[stop], total_price)
        for next_stop, price in self.graph[stop]:
            self.finder(next_stop, total_price + price, nstops + 1)

    def find_cheapest_prices_dijikstra(self, n, flights, src, dst, k):
        import heapq
        graph = self.build_graph(flights, n)
        prior_q = [(0, 0, src)]
        paths = {}
        while prior_q:
            total_prices, nstops, prev_stop = heapq.heappop(prior_q)
            if nstops > k + 1:
                continue
            if total_prices > paths.get((prev_stop, nstops), float("inf")):
                continue
            if prev_stop == dst:
                return total_prices
            for stop, price in graph[prev_stop]:
                if total_prices + price < paths.get((stop, nstops + 1), float("inf")):
                    paths[stop, nstops + 1] = total_prices + price
                heapq.heappush(prior_q, (total_prices + price, nstops + 1, stop))
        print(paths)
        return -1

    def find_cheapest_prices_bfs(self, n, flights, src, dst, k):
        graph = self.build_graph(flights, n)
        queue = [(0, 0, src)]
        paths = {x: float("inf") for x in range(n)}
        while queue:
            total_price, nstops, prev_stop = queue.pop()
            for stop, price in graph[prev_stop]:
                if nstops > k + 1:
                    continue
                paths[stop] = min(paths[stop], total_price + price)
                queue.append((total_price + price, nstops + 1, stop))
        print(paths)
        return -1 if paths[dst] == float("inf") else paths[dst]

    def test(self):
        print(self.find_cheapest_prices_dijikstra(3,
                                                  [[0, 1, 100], [1, 2, 100],
                                                      [0, 2, 500]],
                                                  0,
                                                  2,
                                                  1))


Solution().test()
