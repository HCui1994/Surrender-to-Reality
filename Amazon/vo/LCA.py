class LCA(object):
    def lca(self, root, p, q):

        lca_node = root
        lca_level = 0
        terminate = False

        def postorder(node, level):
            nonlocal lca_node, lca_level, terminate
            if not node:
                return False
            if terminate:
                return True
            left = postorder(node.left, level + 1)
            right = postorder(node.right, level + 1)
            curr = node == p or node == q
            flag = curr + left + right
            if flag == 2 and level > lca_level:
                lca_node = node
                lca_level = level
                terminate = True
            return flag > 0

        postorder(root)
        return lca_node


if __name__ == "__main__":
    import sys
    sys.path.append("../../")
    from playground.TreePlayground import BinaryTreeUtil, TreeNode
    root = BinaryTreeUtil.build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    BinaryTreeUtil.pretty_print_tree(root)
