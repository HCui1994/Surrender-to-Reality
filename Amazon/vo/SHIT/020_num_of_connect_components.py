class ConnectComponentsCounter(object):
    def counter(self, n, edges):
        self.graph = self._build_graph(edges)
        self.visied = set()
        cnt = 0
        for v in range(n):
            if v in self.graph and v not in self.visied:
                self._dfs(v)
                cnt += 1
        return cnt

    def _dfs(self, v):
        if v in self.visied:
            return
        self.visied.add(v)
        for u in self.graph:
            self._dfs(u)

    def _build_graph(self, edges):
        import collections
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add[v]
            graph[v].add[u]
        return graph


    # def union_find(self, n, edges):
        