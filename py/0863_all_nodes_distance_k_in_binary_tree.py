"""
We are given a binary tree (with root node root), a target node, and an integer value K.
Return a list of the values of all nodes that have a distance K from the target node.  
The answer can be returned in any order.

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
Output: [7,4,1]
Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.

Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 
Note:
1.  The given tree is non-empty.
2.  Each node in the tree has unique values 0 <= node.val <= 500.
3.  The target node is a node in the tree.
4.  0 <= K <= 1000.
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

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])




class Solution:
    def distance_k_convert_tree_to_graph(self, root : TreeNode, target : TreeNode, k : int):
        """
        将树转为图
        """
        graph = {root.val : set([])}
        if root.left:
            graph[root.val].add(root.left.val)
            self._build_graph(root.left, root, graph)
        if root.right:
            graph[root.val].add(root.right.val)
            self._build_graph(root.right, root, graph)
        res = []
        visited = set([])
        # print(target)
        self._traverse(target.val, k, 0, graph, visited, res)
        return res
        

    def _build_graph(self, node : TreeNode, parent : TreeNode, graph):
        graph[node.val] = set([parent.val])
        if node.left:
            graph[node.val].add(node.left.val)
            self._build_graph(node.left, node, graph)
        if node.right:
            graph[node.val].add(node.right.val)
            self._build_graph(node.right, node, graph)

    def _traverse(self, node, k, dist, graph, visited, res):
        if node in visited:
            return
        if k == dist:
            res.append(node)
            return
        visited.add(node)
        for succ in graph[node]:
            self._traverse(succ, k, dist + 1, graph, visited, res)


    def distance_k_2(self, root : TreeNode, target : TreeNode, k : int):
        """
        另一种方法，为每个 node 添加一个 parent 属性，一个 visited 属性，从而转换为图
        """
        root.parent = None
        root.visited = False
        target_node = []
        self._add_attr(root.left, root, target.val, target_node)
        self._add_attr(root.right, root, target.val, target_node)
        target = target_node[0]
        res = []
        print(target.__dict__)
        self._traverse_2(target, k, 0, res)
        print(res)


    def _add_attr(self, node : TreeNode, parent : TreeNode, target_val, target_node):
        if node:
            if node.val == target_val:
                target_node.append(node)
            node.parent = parent
            node.visited = False
            self._add_attr(node.left, node, target_val, target_node)
            self._add_attr(node.right, node, target_val, target_node)
            # print(node.__dict__)
        
    def _traverse_2(self, node : TreeNode, k, dist, res):
        if not node:
            return
        if node.visited:
            return
        if dist == k:
            res.append(node.val)
            return
        node.visited = True
        self._traverse_2(node.left, k, dist + 1, res)
        self._traverse_2(node.right, k, dist + 1, res)
        self._traverse_2(node.parent, k, dist + 1, res)

    def _distance_k_3(self, root : TreeNode, target : TreeNode, k : int):
        """
        从某个节点开始，如果 target 在左子树中，距离该节点 d，则找到右子树中深度 k - d 的节点
        """
        target_node = []
        self._add_attr(root.left, root, target.val, target_node)
        self._add_attr(root.right, root, target.val, target_node)
        target = target_node[0]

        res = []
        self._traverse_3(root, target, k, res)
        print(res)
        return res

    def _traverse_3(self, node : TreeNode, target : TreeNode, k, res):
        if not node:
            return -1
        if node is target:
            self._sub_tree_add(node, k, 0, res)
            return 1
        left, right = self._traverse_3(node.left, target, k, res), self._traverse_3(node.right, target, k, res)
        if left != -1:
            if left == k:
                res.append(node.val)
            self._sub_tree_add(node.right, k, left + 1, res)
            return left + 1
        elif right != -1:
            if right == k:
                res.append(node.val)
            self._sub_tree_add(node.left, k, right + 1, res)
            return right + 1
        else:
            return -1

    def _sub_tree_add(self, node, k, d, res):
        if not node:
            return
        if d == k:
            res.append(node.val)
        else:
            self._sub_tree_add(node.left, k, d + 1, res)
            self._sub_tree_add(node.right, k, d + 1, res)

def test():
    tree = "[3,5,1,6,2,0,8,null,null,7,4]"
    root = stringToTreeNode(tree)
    target = stringToTreeNode("[5]")
    k = 2
    Solution()._distance_k_3(root, target, k)


if __name__ == "__main__":
    test()