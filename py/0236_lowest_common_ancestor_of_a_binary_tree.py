"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants 
(where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5

Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
             according to the LCA definition.

Note:
1.  All of the nodes' values will be unique.
2.  p and q are different and both values will exist in the binary tree.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self._confirmed = False
        self._lca = None

    def lowest_common_ancestor_recursive(self, root, p, q):
        """
        后序遍历，第一个 left, right, itself 出现两个 true 的节点即为所求
        """
        self._postorder(root, p, q)
        return self._lca

    def _postorder(self, node, p, q):
        if self._confirmed:
            return 2
        itself = left = right = 0
        if node.val == p or node.val == q:
            itself = 1
        if node.left:
            left = self._postorder(node.left, p, q)
        if node.right:
            right = self._postorder(node.right, q, p)
        if sum([itself, left, right]) == 2 and not self._confirmed:
            self._lca = node
            self._confirmed = True
            return 2
        else:
            return sum([itself, left, right])


    def lowest_common_ancestor_iterative_without_parent_pointer(self, root, p, q):
        stack = [root]
        lca_index = None
        while stack:
            node = stack.pop()
            if (node == p or node == q) and lca_index is None:
                lca_index = len(stack)
            else:
                return stack[lca_index]
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        

        