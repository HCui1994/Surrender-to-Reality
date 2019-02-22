from functools import singledispatch


class Dijikstra(object):

    def shortest_path_min_heap(self, n, src, edges=None, adj_mat=None, mode="edges"):
        import heapq
        graph = self.build_graph(n, edges=edges, adj_mat=adj_mat, mode=mode)
        paths = {x: (float("inf"), []) for x in range(n)}
        paths[src] = (0, [src])
        priority_queue = [(0, [src])]
        while priority_queue:
            cum_w, path = heapq.heappop(priority_queue)
            u = path[-1]
            for v in graph[u]:
                w = graph[u][v]
                if cum_w + w < paths[v][0]:
                    paths[v] = (cum_w + w, path + [v])
                    heapq.heappush(priority_queue, (cum_w + w, path + [v]))
        print(paths)

    def build_graph(self, n, edges=None, adj_mat=None, mode="edges"):
        import collections
        graph = collections.defaultdict(dict)
        if mode == "edges":
            for u, v, w in edges:
                graph[u][v] = w
        elif mode == "adj_matrix":
            for u in range(n):
                for v in range(n):
                    if adj_mat[u][v] == 0:
                        continue
                    graph[u][v] = adj_mat[u][v]
        return graph

    def build_graph_adjacency_matrix(self, matrix):
        import collections

    def test(self):
        # n = 4
        # edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 2, 100]]
        # src = 1
        n = 6
        adj_mat = [[0, 2, 1, 4, 5, 1],
                   [1, 0, 4, 2, 3, 4],
                   [2, 1, 0, 1, 2, 4],
                   [3, 5, 2, 0, 3, 3],
                   [2, 4, 3, 4, 0, 1],
                   [3, 4, 7, 3, 1, 0]]
        src = 0
        self.shortest_path_min_heap(
            n, src=src, adj_mat=adj_mat, mode="adj_matrix")


Dijikstra().shortest_path_1_test()
