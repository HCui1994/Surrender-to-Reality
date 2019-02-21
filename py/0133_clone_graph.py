"""
Given the head of a graph, return a deep copy (clone) of the graph. 
Each node in the graph contains a label (int) and a list (List[UndirectedGraphNode]) of its neighbors. 
There is an edge between the given node and each of the nodes in its neighbors.

OJ's undirected graph serialization (so you can understand error output):
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
 
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
 

Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/

Note: 
The information about the tree serialization is only meant so that you can understand error output if you get a wrong answer. 
You don't need to understand the serialization to solve the problem.
"""

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def clone_graph(self, node):
        if not node:
            return None
        node_mapping = {}
        new_node = UndirectedGraphNode(node.label)
        visited = set()
        self._build_nodes(node, new_node, node_mapping, visited)
        visited = set()
        self._build_links(node, node_mapping, visited)
        return new_node

    def _build_nodes(self, old_node, new_node, node_mapping, visited):
        if old_node in visited:
            return
        visited.add(old_node)
        node_mapping[old_node] = new_node
        for old_node_neighbor in old_node.neighbors:
            new_node_neighbor = UndirectedGraphNode(old_node_neighbor.label)
            self._build_nodes(old_node_neighbor, new_node_neighbor, node_mapping, visited)
    
    def _build_links(self, old_node, node_mapping, visited):
        if old_node in visited:
            return 
        visited.add(old_node)
        new_node = node_mapping[old_node]
        for old_node_neighbor in old_node.neighbors:
            new_node.neighbors.append(node_mapping[old_node_neighbor])
            self._build_links(old_node_neighbor, node_mapping, visited)
        