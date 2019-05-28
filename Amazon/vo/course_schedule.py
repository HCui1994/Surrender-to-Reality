# topological order
# eigher using dfs, or bfs
# if there exists a topological order, either is find
# if there may exist circle, use bfs
# bfs: it can detect circle dependency

# build a graph,
# record the indgree
# find a course, no prequisite: entrance of bfs
# bfs: visit a node, decrease the indegree of its successors, put it into out seq
# bfs finished: if all the nodes are visited => no circle, out_seq is the order
# if not

import collections


class CourseScheduler(object):
    def topological_order_bfs(self, num_courses, prerequisites):
        # no corner case
        graph, indegree = self._build_graph(prerequisites)
        starts = set(range(num_courses)) - indegree.keys()
        order = []
        queue = collections.deque()
        for s in starts:
            queue.append(s)
            while queue:
                v = queue.popleft()
                order.append(v)
                for u in graph[v]:
                    indegree[u] -= 1
                    if indegree[u] == 0:
                        queue.append(u)
        if len(order) != num_courses:
            print("circle exists")
            return order
        return order

    def topological_order_dfs(self, num_courses, prerequisite):
        self.graph, indegree = self._build_graph(prerequisite)
        starts = set(range(num_courses)) - indegree.keys()
        self.order = []
        self.visited = set()
        for s in starts:
            self._dfs(s)
        print(self.order)

    def _dfs(self, v):
        if v in self.visited:
            return
        self.visited.add(v)
        for u in self.graph[v]:
            self._dfs(u)
        self.order.append(v)

    def _build_graph(self, prerequisites):
        graph = collections.defaultdict(set)
        indegree = collections.Counter()
        for course, pre in prerequisites:
            graph[pre].add(course)
            indegree[course] += 1
        return graph, indegree


if __name__ == "__main__":
    course_scheduler = CourseScheduler()
    course_scheduler.topological_order_dfs(3, [[1, 0], [1, 2], [0, 1]])
