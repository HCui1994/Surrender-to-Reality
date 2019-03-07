"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def is_balanced(self, root: TreeNode):
        if not root:
            return True
        return self.traverse(root) != -1

    def traverse(self, node):
        if not node:
            return 0
        left = self.traverse(node.left)
        if left == -1:
            return -1
        right = self.traverse(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1


if __name__ == "__main__":
    import sys
    sys.path.append("..")
    from playground.TreePlayground import BinaryTreeUtil
    root = BinaryTreeUtil.build_tree([1, 1, 1, 1, 1, None, 1])
    BinaryTreeUtil.pretty_print_tree(root)
    soln = Solution()
    print(soln.is_balanced(root))
