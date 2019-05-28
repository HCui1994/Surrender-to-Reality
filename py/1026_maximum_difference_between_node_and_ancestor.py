"""
Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)

Example 1:
Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: 
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
"""
class TreeNode(object):
    def __init__(self, x, *args, **kwargs):
        self.val = x
        self.left = self.right = None
        return super().__init__(*args, **kwargs)


class Solution(object):
    def max_ancestor_diff(self, root: TreeNode) -> int:
        self.global_max_diff = 0
        self.postorder(root)
        return self.global_max_diff

    def postorder(self, node: TreeNode) -> int:
        if not node.left and not node.right:
            return node.val, node.val
        if node.left and not node.right:
            left_min, left_max = self.postorder(node.left)
            local_max_diff = max(abs(node.val - left_min), abs(node.val - left_max))
            self.global_max_diff = max(self.global_max_diff, local_max_diff)
            return min(node.val, left_min), max(node.val, left_max)
        if not node.left and node.right:
            right_min, right_max = self.postorder(node.right)
            local_max_diff = max(abs(node.val - right_min), abs(node.val - right_max))
            self.global_max_diff = max(self.global_max_diff, local_max_diff)
            return min(node.val, right_min), max(node.val, right_max)
        if node.left and node.right:
            left_min, left_max = self.postorder(node.left)
            right_min, right_max = self.postorder(node.right)
            local_max_diff = max(abs(node.val - left_min), abs(node.val - left_max), abs(node.val - right_min), abs(node.val - right_max))
            self.global_max_diff = max(self.global_max_diff, local_max_diff)
            return min(node.val, left_min, right_min), max(node.val, left_max, right_max)