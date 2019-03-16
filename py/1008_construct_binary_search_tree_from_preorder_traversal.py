# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        self.root = None
        for val in preorder:
            self.root = self.insert(val)
        return self.root

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            node = self.root
            is_left = True
            while node:
                parent = node
                if val < node.val:
                    node = node.left
                    is_left = True
                else:
                    node = node.right
                    is_left = False
            if is_left:
                parent.left = TreeNode(val)
            else:
                parent.right = TreeNode(val)
        return self.root