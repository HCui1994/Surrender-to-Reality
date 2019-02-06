"""
Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
 
Note:
1 <= pre.length == post.length <= 30
pre[] and post[] are both permutations of 1, 2, ..., pre.length.
It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def construct_from_pre_post(self, pre, post):
        if not pre and not post:
            return None
        node = TreeNode(pre[0])
        pre = pre[1:]
        post = post[:-1]
        pre_set, post_set = set(), set()
        for idx in range(len(pre)):
            pre_set.add(pre[idx])
            post_set.add(post[idx])
            if pre_set == post_set:
                break
        node.left = self.construct_from_pre_post(pre[:idx], post[idx:])
        node.right = self.construct_from_pre_post(pre[:idx], post[idx:])
        return node