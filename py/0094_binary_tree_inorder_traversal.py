"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [1,3,2]

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorder_traversal_recursive(self, root: TreeNode):
        res = []
        self.inorder_recursive_helper(root, res)
        return res

    def inorder_recursive_helper(self, node: TreeNode, res):
        if not node:
            return 
        self.inorder_recursive_helper(node.left, res)
        res.append(node.val)
        self.inorder_recursive_helper(node.right, res)

    def inorder_traversal_iterative(self, root: TreeNode):
        if not root:
            return []
        res = []
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res
