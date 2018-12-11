"""
Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:
1.  The left subtree of a node contains only nodes with keys less than the node's key.
2.  The right subtree of a node contains only nodes with keys greater than the node's key.
3.  Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true

Example 2:
    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.

1120 -> 1134 (ac)
99.73%
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def is_valid_bst(self, root: TreeNode):
        if not root:
            return True
        return self._dfs(root, -float("inf"), float("inf"))

    def _dfs(self, node : TreeNode, lower_bound, upper_bound):
        if not (node.val < upper_bound and node.val > lower_bound):
            return False
        valid = True
        if node.left:
            valid = valid and self._dfs(node.left, lower_bound, node.val)
        if not valid:
            return False
        if node.right:
            valid = valid and self._dfs(node.right, node.val, upper_bound)
        return valid