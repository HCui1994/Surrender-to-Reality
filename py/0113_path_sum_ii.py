"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

Return:
[
   [5,4,11,2],
   [5,8,4,5]
]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def path_sum(self, root, sum):
        res = []
        self._traverse(root, sum, 0, [], res)
        return res

    def _traverse(self, node : TreeNode, sum, curr_sum, path, res):
        if not node.left and not node.right:
            if curr_sum + node.val == sum:
                res.append(path + [node.val])
        if node.left:
            self._traverse(node.left, sum, curr_sum + node.val, path + [node.val], res)
        if node.right:
            self._traverse(node.right, sum, curr_sum + node.val, path + [node.val], res)