"""
Given a non-empty binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 
The path must contain at least one node and does not need to go through the root.

Example 1:
Input: [1,2,3]

       1
      / \
     2   3
Output: 6

Example 2:
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7
Output: 42
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def max_path_sum(self, root: TreeNode):
        """
        在每个节点计算经过该节点的最大路径长度
        """
        self.res = -float("inf")
        self.max_gain(root)
        return self.res

    def max_gain(self, node: TreeNode):
        if not node:
            return 0
        left_gain = max(self.max_gain(node.left), 0)
        right_gain = max(self.max_gain(node.right), 0)
        self.res = max(self.res, left_gain + right_gain + node.val)
        return max(left_gain, right_gain) + node.val