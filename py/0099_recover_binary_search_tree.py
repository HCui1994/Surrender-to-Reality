"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def recover_tree_recursive(self, root: TreeNode):
        self.previous = TreeNode(-float("inf"))
        self.first = self.second = None
        
    def preorder_traverse(self, node: TreeNode):
        if not node:
            return 
        self.preorder_traverse(node.left)
        if node.val < self.previous.val and not self.first:
            self.first = self.previous
        if node.val < self.previous.val and self.first:
            self.secon = node
        self.previous = node
        self.preorder_traverse(node.right)



    def recover_tree_trivial(self, root: TreeNode):
        self.nodes = []
        self.vals = []
        self.inorder_traverse(root)
        self.vals.sort()
        for node, val in zip(self.nodes, self.vals):
            node.val = val
        
    def inorder_traverse(self, node: TreeNode):
        if not node:
            return
        self.inorder_traverse(node.left)
        self.nodes.append(node)
        self.vals.append(node.val)
        self.inorder_traverse(node.right)