"""
Given a binary tree where every node has a unique value, and a target key k, find the value of the nearest leaf node to target k in the tree.
Here, nearest to a leaf means the least number of edges travelled on the binary tree to reach any leaf of the tree. 
Also, a node is called a leaf if it has no children.
In the following examples, the input tree is represented in flattened form row by row. The actual root tree given will be a TreeNode object.

Example 1:
Input:
root = [1, 3, 2], k = 1
Diagram of binary tree:
          1
         / \
        3   2
Output: 2 (or 3)
Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.

Example 2:
Input:
root = [1], k = 1
Output: 1
Explanation: The nearest leaf node is the root node itself.

Example 3:
Input:
root = [1,2,3,4,null,null,null,5,null,6], k = 2
Diagram of binary tree:
             1
            / \
           2   3
          /
         4
        /
       5
      /
     6
Output: 3
Explanation: The leaf node with value 3 (and not the leaf node with value 6) is nearest to the node with value 2.

Note:
1.  root represents a binary tree with at least 1 node and at most 1000 nodes.
2.  Every node has a unique node.val in range [1, 1000].
3.  There exists some node in the given binary tree for which node.val == k.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def stringToTreeNode(input):
        input = input.strip()
        input = input[1:-1]
        if not input:
            return None

        inputValues = [s.strip() for s in input.split(',')]
        root = TreeNode(int(inputValues[0]))
        nodeQueue = [root]
        front = 0
        index = 1
        while index < len(inputValues):
            node = nodeQueue[front]
            front = front + 1

            item = inputValues[index]
            index = index + 1
            if item != "null":
                leftNumber = int(item)
                node.left = TreeNode(leftNumber)
                nodeQueue.append(node.left)

            if index >= len(inputValues):
                break

            item = inputValues[index]
            index = index + 1
            if item != "null":
                rightNumber = int(item)
                node.right = TreeNode(rightNumber)
                nodeQueue.append(node.right)
        return root


class Solution:
    # def find_closest_leaf(self, root : TreeNode, k):
    #     """
    #     只有两种可能：
    #     1.  要找的节点到最近叶节点的距离
    #     2.  要找的节点的某个祖先到 k 的距离，与该祖先节点到
    #     """
    #     pass

    # def _traverse(self, root : TreeNode, k, depth):
    #     # 1. 算每个节点的深度
    #     # 2. 算每个节点的高度
    #     if not root.left and not root.right:
    #         return 1
    #     left_height, right_height = self._traverse(root.left, k), self._traverse(root.right, k)
    #     height = min(left_height, right_height)
    #     depth = depth + 1

    def __init__(self):
        self._root = None
        self._min_height = {}

    def find_closest_leaf_tree_to_graph(self, root : TreeNode, k):
        """
        将树转换为无向无环图，再做 dfs 
        """
        self._root = root.val
        graph = {root.val : set([])}
        if root.left:
            self._build_graph(root.left, root, graph)
        if root.right:
            self._build_graph(root.right, root, graph)
        visited = set([])
        tip = {}
        self._dfs(k, graph, visited, tip, 0)
        path_length = float("inf")
        nearest = root.val
        for node, dist in tip.items():
            if dist < path_length:
                path_length, nearest = dist, node
        return nearest

    def _build_graph(self, node : TreeNode, parent : TreeNode, graph):
        graph[node.val] = set([])
        graph[node.val].add(parent.val)
        graph[parent.val].add(node.val)
        if not node.left and not node.right:
            return
        if node.left:
            self._build_graph(node.left, node, graph)
        if node.right:
            self._build_graph(node,right, node, graph)
        
    def _dfs(self, node, graph, visited, tip, path_length):
        if node in visited:
            return
        visited.add(node)
        path_length += 1
        succ_set = graph[node]
        if len(succ_set) == 1 and node.val != self._root:
            tip[node] = path_length
            return
        for succ in succ_set:
            self._dfs(succ, graph, visited, tip, path_length)
        
    def find_closest_leaf_2(self, root : TreeNode, k):
        """
        对于每个内部节点，都可以算出最小高度。用一次遍历记录这个最小高度        
        与目标最近的叶节点与目标必有公共最低祖先节点
        """
        min_height = {}
        dist_to_k = {}
        self._record_min_heieght(root, min_height)
        for key in min_height:
            dist_to_k[key] = float("inf")
        self._dist_to_target(root, k, dist_to_k)
        nearest = float("inf")
        nearest_leaf = None
        return min(dist_to_k[node] + min_height[node] for node in dist_to_k.keys())
    
    def _record_min_heieght(self, node : TreeNode, min_height):
        if not node.left and not node.right:
            min_height[node.val] = 0
            return 0
        left_height, right_height = float("inf"), float("inf")
        if node.left:
            left_height = min(left_height, self._record_min_heieght(node.left, min_height))
        if node.right:
            right_height = min(right_height, self._record_min_heieght(node.right, min_height))
        min_height[node.val] = min(left_height, right_height) + 1
        return min_height[node.val]

    def _dist_to_target(self, node : TreeNode, k, dist_to_k):
        if not node:
            return float("inf")
        if node.val == k:
            dist_to_k[node.val] = 0
            return 0
        dist_to_k[node.val] = min(self._dist_to_target(node.left, k, dist_to_k), self._dist_to_target(node.right, k, dist_to_k)) + 1
        return dist_to_k[node.val]
            



def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def test():
    string = "[1,2,3,4,null,null,null,5,null,6]"
    root = stringToTreeNode(string);
    k = 4
            
    ans = Solution().find_closest_leaf_2(root, k)
    print(ans)

if __name__ == '__main__':
    test()