"""
Given an undirected graph, return true if and only if it is bipartite.
Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B
such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  
Each node is an integer between 0 and graph.length - 1.  
There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.

Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.

Note:

1.  graph will have length in range [1, 100].
2.  graph[i] will contain integers in range [0, graph.length - 1].
3.  graph[i] will not contain i or duplicate values.
4.  The graph is undirected: if any element j is in graph[i], then i will be in graph[j].
"""

class Solution:
    def is_bipartite_bfs(self, graph):
        """
        二分图问题
        如果两个 vertice 之间有 edge，则必然不可能在同一个 set 中
        不能按照任意顺序来访问边，应采用 bfs 或 dfs，需要 visited 列表保存已访问过的节点
        注意，可能不是连通图
        每次访问到一个节点，根据遍历过程中其前置节点，将它添加到 A 或 B 某个集合中。注意，已经访问到的节点若再次遍历到，还应再添加一遍
        最后若两个集合有交集，则必然不是二分图
        """
        if not graph:
            return True
        sets = {True: set([]), False: set([])}
        visited = set([])
        for v in range(len(graph)):
            if not v in visited:
                queue = []
                queue.append((v, True))
                while queue:
                    v1, tag= queue.pop(0)
                    sets[tag].add(v1)
                    if v1 in sets[not tag]:
                        return False
                    if v1 in visited:
                        continue
                    visited.add(v1)
                    for v2 in graph[v1]:
                        queue.append((v2, not tag))
        return sets[True] - sets[False] == sets[True]
    
    def is_bipartite_dfs(self, graph):
        if not graph:
            return True
        s, t, visited = set([]), set([]), set([])
        for v1 in range(len(graph)):
            if not v1 in visited:
                self._dfs(graph, s, t, visited, v1=v1, flag=True)
        print(s, t)
        return s - t == s

    def _dfs(self, graph, s, t, visited, v1, flag):
        if flag:
            s.add(v1)
        else:
            t.add(v1)
        if v1 in visited:
            return
        visited.add(v1)
        for v2 in graph[v1]:
            self._dfs(graph, s, t, visited, v2, flag=not flag)
    
    def test(self):
        graph = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
        print(self.is_bipartite_bfs(graph))


Solution().test()