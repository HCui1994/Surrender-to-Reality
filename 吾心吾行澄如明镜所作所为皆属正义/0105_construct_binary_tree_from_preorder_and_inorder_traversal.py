"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self._preorder_idx = 0
        self._preorder = None

    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        self._preorder = preorder
        for idx in range(len(inorder)):
            if preorder[self._preorder_idx] == inorder[idx]:
                break
        root = TreeNode(self._preorder[self._preorder_idx])
        self._preorder_idx += 1
        self._build_tree(inorder[:idx], inorder[idx + 1:], root)
        return root

    def _build_tree(self, left_nodes, right_nodes, node):
        if left_nodes:
            # 如果 left_nodes 非空，next_node 一定在 left_nodes 中
            for idx in range(len(left_nodes)):
                if self._preorder[self._preorder_idx] == left_nodes[idx]:
                    break
            node.left = TreeNode(self._preorder[self._preorder_idx])
            self._preorder_idx += 1
            self._build_tree(left_nodes[:idx], left_nodes[idx + 1:], node.left)
        if right_nodes:
            for idx in range(len(right_nodes)):
                if self._preorder[self._preorder_idx] == right_nodes[idx]:
                    break
            node.right = TreeNode(self._preorder[self._preorder_idx])
            self._preorder_idx += 1
            self._build_tree(right_nodes[:idx], right_nodes[idx + 1:], node.right)

        