"""
There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:
Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1].

Example 2:
Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

1.  The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
2.  You may assume that there are no duplicate edges in the input prerequisites.
"""

class Solution:
    def find_order(self, num_courses, prerequisites):
        """
        topological sort
        """
        graph, indegree = self._build_graph(prerequisites)
        all_courses = set(range(num_courses))
        print(all_courses)
        valid, order = self._topological_sort(*self._build_graph(prerequisites))
        if valid:
            return order + list(all_courses - set(order))
        else:
            return []

    def _build_graph(self, edges):
        """ no duplicated edges """
        graph = {}
        indegree = {}
        vertices = set([])
        for prec, succ in edges:
            indegree[prec] = 0
            indegree[succ] = 0
            graph[prec] = set([])
            graph[succ] = set([])
        for succ, prec in edges:
            
            if prec not in graph.keys():
                graph[prec] = set([succ])
            else:
                graph[prec].add(succ)
            indegree[succ] += 1
        return graph, indegree

    def _topological_sort(self, graph, indegree):
        """ BFS topological sort """
        order = []
        queue = []
        for vertice in indegree.keys():
            if indegree[vertice] == 0:
                queue.append(vertice)
                while queue:
                    prec = queue.pop(0)
                    order.append(prec)
                    succ_set = graph[prec]
                    for succ in succ_set:
                        indegree[succ] -= 1
                        if indegree[succ] == 0:
                            # 注意，在此将 indegree 设置为 -1，表示该节点已经完成访问，否则在 in indegree[vertice] == 0 处会有bug
                            indegree[succ] = -1
                            queue.append(succ)
        if len(order) != len(indegree):
            return False, order
        else:
            return True, order
    
    def test(self):
        num_courses = 4
        prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        ans = self.find_order(num_courses, prerequisites)
        print(ans)


soln = Solution()
soln.test()