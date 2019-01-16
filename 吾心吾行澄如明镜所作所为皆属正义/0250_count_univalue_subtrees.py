"""
Given a binary tree, count the number of uni-value subtrees.
A Uni-value subtree means all nodes of the subtree have the same value.

Example :
Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def count_univalue_subtrees(self, root: TreeNode):
        if not root:
            return 0
        _, cnt = self.uni_subtree_counter(root)
        return cnt

    def uni_subtree_counter(self, node):
        if not node.left and not node.right:
            return True, 1
        is_uni, cnt = True, 0
        if node.left:
            is_uni_left, cnt_left = self.uni_subtree_counter(node.left)
            is_uni = is_uni and is_uni_left and (node.val == node.left.val)
            cnt += cnt_left
        if node.right:
            is_uni_right, cnt_right = self.uni_subtree_counter(node.right)
            is_uni = is_uni and is_uni_right and (node.val == node.right.val)
            cnt += cnt_right
        if is_uni:
            return True, cnt + 1
        else:
            return False, cnt

