import sys
sys.path.append("../..")

from playground.TreePlayground import BinaryTreeUtil, TreeNode




class Traversal(object):
    def preorder(self, root: TreeNode):
        if not root:
            return 
        stack = []
        node = root
        while stack or node:
            while node:
                print(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right

    def inorder(self, root: TreeNode):
        if not root:
            return
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            print(node.val)
            node = node.right

    def postorder(self, root: TreeNode):
        if not root:
            return
        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            res.append(node.val)
        print(res[::-1])

root = BinaryTreeUtil.build_tree([1,2,3,4,5,6,7,8,9])
BinaryTreeUtil.pretty_print_tree(root)
Traversal().postorder(root)