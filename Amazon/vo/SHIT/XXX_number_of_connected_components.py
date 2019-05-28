class Solution(object):
    def count_components(self, n, edges):
        parent = [i for i in range(n)]
        for u, v in edges:
            parent[u] = v
        
        def _find(u):
            if parent[u] == u:
                return u
            parent[u] = _find(parent[u])
            return parent[u]

        def _union(u, v):
            root_u, root_v = _find(u), _find(v)
            if root_u == root_v:
                return
            parent[root_u] = root_v
        
        