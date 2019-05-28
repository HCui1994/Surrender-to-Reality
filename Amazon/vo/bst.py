
import sys
sys.path.append("../../")
from playground.TreePlayground import TreeNode, BinaryTreeUtil


class BinarySearchTree(object):
    def __init__(self, values, *args, **kwargs):
        self.root = self.build(values)
        return super().__init__(*args, **kwargs)

    def build(self, values):
        if not values:
            return None
        root = TreeNode(values[0])
        left_values = []
        right_values = []
        for val in values[1:]:
            if val < values[0]:
                left_values.append(val)
            else:
                right_values.append(val)
        root.left = self.build(left_values)
        root.right = self.build(right_values)
        return root

    def delete_node(self, val):
        node = self.root
        parent = None
        while node and node.val != val:
            parent = node
            if val < node.val:
                node = node.left
            else:
                node = node.right
        if not node:
            print("not found")
            return
        if not node.left and not node.right:
            if not parent:  # root node, as well as leaf node
                return None
            if node == parent.left:
                parent.left = None
            else:
                parent.right = None
        elif not node.left and node.right:
            if not parent:
                self.root = node.right
                return
            if node == parent.left:
                parent.left = node.right
            else:
                parent.right = node.right
        elif node.left and not node.right:
            if not parent:
                self.root = node.left
                return
            if node == parent.left:
                parent.left = node.left
            else:
                parent.right = node.left
        elif node.left and node.right:
            predecessor = self.pick_predecessor(node)
            if node == parent.left:
                parent.left = predecessor
            else:
                parent.right = predecessor
            predecessor.right = node.right
            if predecessor == node.left:
                predecessor.left = node.left

            

    def pick_predecessor(self, node):
        parent = node
        node = node.left
        while node.right:
            parent = node
            node = node.right
        if node == parent.left:
            parent.left = None
        else:
            parent.right = None
        print(parent.val, node.val)
        return node

    def get_root(self):
        return self.root


bst = BinarySearchTree([1,2,3,4,7,6,5,9,8])
BinaryTreeUtil.pretty_print_tree(bst.get_root())
bst.delete_node(7)
BinaryTreeUtil.pretty_print_tree(bst.get_root())