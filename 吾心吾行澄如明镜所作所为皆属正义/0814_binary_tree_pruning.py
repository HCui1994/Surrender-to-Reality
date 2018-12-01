"""
We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.
Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

Example 1:
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.

Example 2:
Input: [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]

Example 3:
Input: [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]

Note:
1.  The binary tree will have at most 100 nodes.
2.  The value of each node will only be 0 or 1.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def prune_tree(self, root):
        """
        后序遍历，统计子树的节点值之和。若和为 0，剪枝
        """
        if root.val == 0 and not root.left and not root.right:
            return None
        self._postorder_traverse(root)
        return root

    def _postorder_traverse(self, node : TreeNode):
        if not node:
            return 0
        left = self._postorder_traverse(node.left)
        right = self._postorder_traverse(node.right)
        if not left:
            node.left = None
        if not right:
            node.right = None
        return left + right + node.val
        