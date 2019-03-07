class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = self.right = None


class RBNode(object):
    def __init__(self, x):
        pass


class BinaryTreeUtil(object):
    @staticmethod
    def build_tree(inputs):
        root = TreeNode(int(inputs[0]))
        node_queue = [root]
        front = 0
        index = 1
        while index < len(inputs):
            node = node_queue[front]
            front = front + 1
            item = inputs[index]
            index = index + 1
            if item != None:
                node.left = TreeNode(item)
                node_queue.append(node.left)
            if index >= len(inputs):
                break
            item = inputs[index]
            index = index + 1
            if item != None:
                node.right = TreeNode(item)
                node_queue.append(node.right)
        return root

    @staticmethod
    def pretty_print_tree(root):
        def printer(node, prefix="", is_left=True):
            if not node:
                print("Empty Tree")
                return
            if node.right:
                printer(node.right, prefix + ("│   " if is_left else "    "), False)
            print(prefix + ("└── " if is_left else "┌── ") + str(node.val))
            if node.left:
                printer(node.left, prefix + ("    " if is_left else "│   "), True)
        printer(root)