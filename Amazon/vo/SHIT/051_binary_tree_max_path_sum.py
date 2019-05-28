import sys  
sys.path.append("../../..")
from playground.TreePlayground import BinaryTreeUtil, TreeNode

class PathSum(object):
    def max_path_sum(self, root):
        self.res = -float("inf")
        self.max_gain(root)

    def max_gain(self, node):
        if not node:
            return 0
        left_gain = max(0, self.max_gain(node.left))
        right_gain = max(0, self.max_gain(node.right))
        self.res = max(self.res, left_gain + right_gain + node.val)
        return max(left_gain, right_gain) + node.val