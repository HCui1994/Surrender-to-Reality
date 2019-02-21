"""
There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:
Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""


class Solution(object):
    def can_finish_dfs(self, num_courses, prerequisites):
        """
        在有向图中寻找环的问题
        在环内的所有课程都无法修习，因为存在死锁
        有效的计数是在环外的节点数量
        若用 bfs 解决本题目：
        建立 graph 与 indegree 数据结构，从任意节点开始遍历，每当访问到一个新节点，其入度自减 1，若其入度为 0，入队
        """
        pass

    def can_finish_bfs(self, num_courses, prerequisites):
        """
        若用 dfs 解决本题目：
        从入度为 0 的节点开始遍历，并建立 visisted 集合。如果在过程中出现新到节点已在 visited 集合中，则图中存在环
        问题是，如何找到起始节点到环入口的路径长度？
        """
        if not num_courses or not prerequisites:
            return True
        graph, indegree = self._build_graph(prerequisites, num_courses)
        print(graph, indegree)
        queue = [node for node in indegree.keys() if indegree[node] == 0]
        num_courses_available = 0
        while queue:
            prec = queue.pop(0)
            num_courses_available += 1
            for succ in graph[prec]:
                indegree[succ] -= 1
                if indegree[succ] == 0:
                    queue.append(succ)
        if num_courses_available < len(graph):
            return False
        else:
            return True

    def can_finishe_dfs(self, num_courses, prerequisites):
        graph, indegree = self._build_graph(prerequisites, num_courses)
        topo_seq = []
        for v in indegree:
            if indegree[v] == 0:
                visited = [0 for _ in range(num_courses)]
                if not self._dfs(v, graph, visited, topo_seq):
                    return False
        if len(topo_seq) < num_courses:
            return False
        return True

    def _dfs(self, v, graph, visited, topo_seq):
        print(v, visited)
        if visited[v] == -1:
            return False
        if visited[v] == 1:
            return True
        visited[v] = -1
        for u in graph[v]:
            if not self._dfs(u, graph, visited, topo_seq):
                return False
        visited[v] = 1
        topo_seq.append(v)
        return True


    def _build_graph(self, edges, num_v):
        graph = {x: set() for x in range(num_v)}
        indegree = {x: 0 for x in range(num_v)}
        for edge in edges:
            graph[edge[0]].add(edge[1])
            indegree[edge[1]] += 1
        return graph, indegree

    def test(self):
        print(self.can_finishe_dfs(8,
                                   [[1, 0], [2, 6], [1, 7], [5, 1], [6, 4], [7, 0], [0, 5]]))


Solution().test()
