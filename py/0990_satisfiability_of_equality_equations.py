import collections


class Solution(object):
    def build_graph(self, edges):
        graph = collections.defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        return graph

    def equations_possible(self, equations):
        eq = []
        neq = []
        for equation in equations:
            a, op, b = equation[0], equation[1], equation[-1]
            if op == '=':
                eq.append((a, b))
            else:
                neq.append((a, b))
        self.graph = self.build_graph(eq)
        print(self.graph)
        for a, b in neq:
            self.target = b
            self.visited = set()
            if not self.dfs(a):
                return False
        return True

    def dfs(self, v):
        print(v, self.target)
        if v == self.target:
            return False
        if v in self.visited:
            return True
        self.visited.add(v)
        for u in self.graph[v]:
            if not self.dfs(u):
                return False
        self.visited.remove(v)
        return True

    def test(self):
        print(self.equations_possible(["c==c", "f!=a", "f==b", "b==c"]))


Solution().test()
