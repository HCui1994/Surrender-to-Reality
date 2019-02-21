"""previous 0212 house robber II"""
"""DFS+DP"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

""" not sure whether this is a DP problem"""
class Solution:
    def rob(self, root):
        return max(self.postorder_rob(root))
    def postorder_rob(self, node):
        if not node:
            return [0, 0]
        rob_left, not_rob_left = self.postorder_rob(node.left)
        rob_right, not_rob_right = self.postorder_rob(node.right)
        rob_current = not_rob_left + not_rob_right + node.val
        not_rob_current = max(rob_left, not_rob_left) + max(rob_right, not_rob_right)
        print(rob_current, not_rob_current)
        return rob_current, not_rob_current
        
