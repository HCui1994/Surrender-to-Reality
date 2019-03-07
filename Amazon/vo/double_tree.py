import sys
sys.path.append("../../")
from playground.TreePlayground import BinaryTreeUtil, TreeNode

root = BinaryTreeUtil.build_tree([1, 2, 3])
BinaryTreeUtil.pretty_print_tree(root)
print("=====")

def double_tree(node: TreeNode):
    if not node:
        return
    left_child = node.left
    node.left = TreeNode(node.val)
    node.left.left = left_child
    double_tree(left_child)
    double_tree(node.right)

double_tree(root)
BinaryTreeUtil.pretty_print_tree(root)