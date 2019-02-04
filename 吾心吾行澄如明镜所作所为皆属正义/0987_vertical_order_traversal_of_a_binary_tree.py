

# Definition for a binary tree node.
import collections
import bisect

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def verticalTraversal(self, root: 'TreeNode') -> 'List[List[int]]':
        self.vertical = collections.defaultdict(collections.defaultdict(list))
        self.preorder(0, 0, root)
        print(self.vertical)

    def preorder(self, x, y, node: TreeNode):
        if not node:
            return
        bisect.insort(self.vertical[x][y], node.val)
        self.preorder(x - 1, y - 1, node.left)
        self.preorder(x + 1, y - 1, node.right) 
        


