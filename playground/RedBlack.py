class RBTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = self.right = self.parent = None
        self.size = None
        self.color = "black"


class RedBlack(object):
    def __init__(self):
        self.nil = RBTreeNode(0)
        self.root = self.nil

    