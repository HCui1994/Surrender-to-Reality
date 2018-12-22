class TreeNode:
    def __init__(self, val):
        self._value = val
        self._left = self._right = None

    def _get_left(self):
        return self._left

    def _get_right(self):
        return self._right

    def _get_value(self):
        return self._value

    def _set_left(self, node):
        self._left = node

    def _set_right(self, node):
        self._right = node

    def _set_value(self, val):
        self._value = val

    left = property(_get_left, _set_left)
    right = property(_get_right, _set_right)
    value = property(_get_value, _set_value)


class TreePlayground:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def chop(self):
        self._root = None

    def initialize_bst(self, node_vals: list):
        self.chop()
        if not list:
            return self._root
        self._root = TreeNode(node_vals[0])
        for node_val in node_vals[1:]:
            # print(node_val)
            curr = self._root
            while curr:
                parent = curr
                if node_val < curr.value:
                    curr = curr.left
                    is_left = True
                else:
                    curr = curr.right
                    is_left = False
            if is_left:
                parent.left = TreeNode(node_val)
            else:
                parent.right = TreeNode(node_val)
        return self._root

    def initialize_from_heap(self, heap: list):
        pass

    def draw_tree(self, node="root", prefix="", is_left=True):
        if node == "root":
            node = self._root
        if not node:
            return
        if node.right:
            self.draw_tree(node.right,
                           prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
        if node.left:
            self.draw_tree(node.left, prefix + ("    " if is_left else "│   "),
                           True)

    def preorder_recursive(self, node="root", res=[]):
        if node == "root":
            node = self._root
        if not node:
            return res
        res.append(node.value)
        self.preorder_recursive(node.left, res)
        self.preorder_recursive(node.right, res)
        return res

    def inorder_recursive(self, node="root", res=[]):
        if node == "root":
            node = self._root
        if not node:
            return res
        self.inorder_recursive(node.left, res)
        res.append(node.value)
        self.inorder_recursive(node.right, res)
        return res

    def postorder_recursive(self, node="root", res=[]):
        if node == "root":
            node = self._root
        if not node:
            return res
        self.postorder_recursive(node.left, res)
        self.postorder_recursive(node.right, res)
        res.append(node.value)
        return res

    def preorder_iterative(self):
        stack = []
        node = self._root
        res = []
        while stack or node:
            while node:
                res.append(node.value)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res

    def inorder_iterative(self):
        stack = []
        node = self._root
        res = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.value)
            node = node.right
        return res

    def postorder_iterative(self):
        if not self._root:
            return []
        stack = [self._root]
        res = []
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            res.append(node.value)
        return res[::-1]

    def levelorder_bfs(self):
        if not self._root:
            return []
        queue = [self._root]
        res = []
        while queue:
            node = queue.pop(0)
            res.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res

    def strict_levelorder_bfs(self):
        if not self._root:
            return []
        queue = [self._root]
        res = []
        while queue:
            level_queue = []
            level_res = []
            for node in queue:
                level_res.append(node.value)
                if node.left:
                    level_queue.append(node.left)
                if node.right:
                    level_queue.append(node.right)
            res.append(level_res)
            queue = level_queue
        return res


def main():
    tree_playground = TreePlayground()
    tree_playground.initialize_bst([5, 3, 8, 1, 9, 0, 4, 7, 2, 6])
    tree_playground.draw_tree()
    print(tree_playground.strict_levelorder_bfs())


if __name__ == "__main__":
    main()