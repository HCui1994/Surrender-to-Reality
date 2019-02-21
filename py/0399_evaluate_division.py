"""
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). 
Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0. 
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: 
vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

== score board ==
19:35 20:22 
1RE
100%
=================
""" 

class Solution:
    def calc_equation(self, equations, values, queries):
        """
        图问题
        先建图，之后dfs
        每个查询的结果即为从分子遍历到分母，路径中边权值的乘积
        """
        graph, edges, vertices = self._build_graph(equations, values)
        res = []
        for molecular, denominator in queries:
            if molecular not in vertices or denominator not in vertices:
                res.append(-1.)
                continue
            visited = set([molecular])
            valid, multiplication = self._dfs(molecular, denominator, 1, edges, graph, visited)
            res.append(multiplication)
        print(res)

    def _dfs(self, m, denominator, multiplication, edges, graph, visited):
        # print(m)
        flag = False
        for d in graph[m]:
            if d == denominator:
                return True, multiplication * edges[m, d]
            if d not in visited:
                visited.add(d)
                valid, mult = self._dfs(d, denominator, multiplication * edges[m, d], edges, graph, visited)
                if valid:
                    return valid, mult
        return False, -1.
        
    def _build_graph(self, equations, values):
        graph = {}
        edges = {}
        vertices = set()
        for i, value in enumerate(values):
            a, b = equations[i]
            vertices.add(a)
            vertices.add(b)
            # 添加自回路
            edges[a, a] = 1.
            edges[b, b] = 1.
            edges[a, b] = values[i]
            edges[b, a] = 1. / values[i]
            if a not in graph.keys():
                graph[a] = set([b])
            else:
                graph[a].add(b)
            graph[a].add(a)
            if b not in graph.keys():
                graph[b] = set([a])
            else:
                graph.add(a)
            graph[b].add(b)
        return graph, edges, vertices

    def test(self):
        equations = [ ["a", "b"], ["b", "c"] ]
        values = [2.0, 3.0]
        queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
        self.calc_equation(equations, values, queries)


Solution().test()