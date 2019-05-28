class LCA(object):
    def lca_recursion(self, root, p, q):
        self.max_depth = -1
        self.lca = None
        self.p, self.q = p, q
        self._postorder(root, 0)
        return self.lca

    def _postorder(self, node, depth):
        if not node:
            return False
        left_flag = self._postorder(node.left, depth + 1)
        right_flag = self._postorder(node.right, depth + 1)
        node_flag = (node == self.p) or (node == self.q)
        if left_flag + right_flag + node_flag >= 2 and depth > self.max_depth:
            self.lca = node
            self.max_depth = depth
        return left_flag or right_flag or node_flag

    def lca_
