class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self, x):
        self.root = TreeNode(x)

    def insert(self, x):
        node = TreeNode(x)
        parent = self.root
        found_position = False
        while not found_position:
            if x <= parent.val and parent.left is not None:
                parent = parent.left
            elif x <= parent.val and parent.left is None:
                parent.left = node
                found_position = True
            elif x > parent.val and parent.right is not None:
                parent = parent.right
            elif x > parent.val and parent.right is None:
                parent.right = node
                found_position = True
    
    def inorder(self):
        series = []
        self._inorder(node=self.root, series=series)
        return series
    
    def _inorder(self, node, series):
        if node is None:
            return 
        self._inorder(node=node.left, series=series)
        series.append(node.val)
        self._inorder(node=node.right, series=series)


# solution using binary serach tree (in-order traverse)   
class Solution:
    def alienOrder(self, words):
        word_lengths = [len(word) - 1 for word in words]
        max_length = max(word_lengths)

        for word in words:
            if len(word) < max_length:
                word += "#" * max_length - len(word)

        dict = set([])
        tree = Tree(words[0][0])
        dict.add(words[0][0])
        for i in range(max_length):
            for j in range(len(words)):
                pass
