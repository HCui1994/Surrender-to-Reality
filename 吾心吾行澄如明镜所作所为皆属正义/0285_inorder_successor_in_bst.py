"""
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
Note: If the given node has no in-order successor in the tree, return null.

Example 1:
Input: root = [2,1,3], p = 1
  2
 / \
1   3
Output: 2

Example 2:
Input: root = [5,3,6,2,4,null,null,1], p = 6
      5
     / \
    3   6
   / \
  2   4
 /   
1

Output: null
"""

# class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorder_successor(self, root, p):
        self.p = p
        self.succ = None
        self.inorder_helper(root)
        return self.succ
    
    def inorder_helper(self, node):
        if not node:
            return
        self.inorder_helper(node.left)
        if node == self.p:
            self.succ = node.right
            return
        self.inorder_helper(node.right)
        
    