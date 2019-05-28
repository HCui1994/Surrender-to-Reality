import sys
sys.path.append("../../..")
from playground.TreePlayground import BinaryTreeUtil, TreeNode

class Codec(object):
    def serialize(self, root):
        res = []
        self._encode(root, res)
        return res
    
    def _encode(self, node, res):
        if not node:
            res.append(None)
            return
        res.append(node.val)
        self._encode(node.left, res)
        self._encode(node.right, res)

    def deserialize(self, data):
        if not data:
            return None
        self.i = 0
        self.data = data
        return self._decode()

    def _decode(self):
        if self.data[self.i] is None:
            self.i += 1
            return None
        root = TreeNode(self.data[self.i])
        self.i += 1
        root.left = self._decode()
        root.right = self._decode()
        return root

if __name__ == "__main__":
    codec = Codec()
    root = BinaryTreeUtil.build_tree([1,2,3,4,5,6,7,8])
    BinaryTreeUtil.pretty_print_tree(root)
    encode = codec.serialize(root)
    print(encode)
    root = codec.deserialize(encode)
    BinaryTreeUtil.pretty_print_tree(root)