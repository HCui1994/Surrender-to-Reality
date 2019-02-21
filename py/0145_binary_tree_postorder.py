"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorder_traversal_recursion(self, root : TreeNode):
        traversal = []
        return self._postorder_traversal(root, traversal)

    def _postorder_traversal(self, node : TreeNode, traversal : list):
        if node.left:
            self._postorder_traversal(node.left, traversal)
        if node.right:
            self._postorder_traversal(node.right, traversal)
        traversal.append(node.val)

    def postorder_traversal_iterative(self, root : TreeNode):
        """
        stack 是干什么用的？保存当前运行时环境！
        如何获取之前的root？
        从 stack 里拿
        """
        if not root:
            return []
        stack = []
        order = []
        stack.append(root)
        while stack:
            root = stack.pop()
            order.append(root.val)
            if root.left: # 先压左子树
                stack.append(root.left)
            if root.right: # 在押右子树
                stack.append(root.right)
        return order[::-1] # 结果逆序

    def preorder_traversal_iterative(self, root : TreeNode):
        if not root:
            return []
        stack = []
        order = []
        stack.append(root)
        while stack:
            root = stack.pop()
            order.append(root.val)
            if root.right: # 先压右子树
                stack.append(root.right)
            if root.left: # 再压左子树
                stack.append(root.left)
        return order    # 结果不用逆序


    def inorder_traversal_itertive(self, root : TreeNode):
        if not root:
            return []
        stack = []
        order = []
        while stack or root:
            while root: # 先沿左子树一路压栈
                stack.append(root)
                root = root.left
            root = stack.pop()
            print(root.val)
            order.append(root.val)
            root = root.right
        return order
            