"""
Given a binary tree, flatten it to a linked list in-place.
For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6

The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self._precursor = None

    def flatten(self, root):
        """
        前序遍历，注意记录前驱节点，将前驱节点指向当前节点
        """
        node_list = []
        self._preorder_traverse(root, node_list)
        # print(node_list)
        for idx in range(0, len(node_list) - 1):
            node_list[idx].left = None
            node_list[idx].right = node_list[idx + 1]
        node_list[-1].left = None
        node_list[-1].right = None
        root = node_list[0]

    def _preorder_traverse(self, node : TreeNode, node_list):
        node_list.append(node)
        if not node.left and not node.right:
            return
        if node.left:
            self._preorder_traverse(node.left, node_list)
        if node.right:
            self._preorder_traverse(node.right, node_list)
    

    def flaten_2(self, root):
        """
        优化空间复杂度
        对于一个节点，其左子树的最右节点是右子的前驱
        """
        pass

    # def _preorder_traverse_2(self, node : TreeNode):
       

        