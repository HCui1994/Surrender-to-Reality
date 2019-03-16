# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_length = 0
        self.postorder(root)
        return self.max_length

    def postorder(self, node):
        if not node:
            return 0
        left = self.postorder(node.left)
        right = self.postorder(node.right)
        self.max_length = max(self.max_length, left + right)
        return max(left, right) + 1