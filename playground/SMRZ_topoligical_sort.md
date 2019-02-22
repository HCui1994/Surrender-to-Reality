# 拓扑排序算法  
当然，是在图数据结构上

---

## DFS

**优点** 无需记录图中节点的入度
**缺点** 若使用深度优先搜索，必须要保证为dag（有向无环图）。
如果在有环图上使用深度优先搜索，算法仍然能够结束，但是无法判断出，该图是有环图。

在深度优先遍历的时候，每到达一个节点，记录当前时间为该节点的开始时间，并且标记该节点为已访问。当结束该节点处的深度优先遍历时，记录当前时间为该节点的结束时间。
最后将所有节点按照结束时间倒序排序，即为拓扑序列。

<pre><code>
def dfs_topological_sort():
    time = 0
    def dfs(v):
        v.inbound_time = time + 1
        v.visited = True
        for u in v.ajd and not u.visited:
            dfs(u)
        v.outbound_time = time + 1
    for v in V and not v.visited:
        dfs(v)
    
    def key(element):
        return element.outbound_time
    
    V = sorted(V, key = key)
</code></pre>

---

## BFS
**优点** 可以判断出图是否有环
**缺点** 需要记录节点的入度，来判断从那个节点开始遍历
<pre><code>
def _topological_sort(self, graph, indegree):
        order = []
        queue = [] # bfs需要的额外数据结构
        for v in V
            v.indegree == 0:
                queue.enqueue(v)
        while queue is not empty:
            precurssor = queue.dequeue(0)
            order.append(precurssor)
            if precurssor has successor:
                for v in successors:
                    v.indegree -= 1
                    if v.indegree == 0: 
                        # 如果有环，在进入搜索时，进入环的节点，入度不可能减到 0
                        # 将会导致没有完成搜索，队列就已经为空
                        queue.enqueue(successor)
        if len(order) == |V|:
        # 如果所有节点都排了序
            return order
        else:
        # 否则，说明图里有环
            return False
</code></pre>