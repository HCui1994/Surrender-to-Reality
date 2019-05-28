import sys
sys.path.append("../../..")
from playground.TreePlayground import BinaryTreeUtil, TreeNode


class Traverser(object):
    def rev_level_order(self, root: TreeNode):
        import collections
        self.res = collections.deque()
        self.rev_level_order_helper(root, 0)
        return self.res
    
    def rev_level_order_helper(self, node: TreeNode, level: int):
        if not node:
            return
        if level + 1 > len(self.res):
            self.res.appendleft([])
        self.res[- (level + 1)].append(node.val)
        self.rev_level_order_helper(node.left, level + 1)
        self.rev_level_order_helper(node.right, level + 1)



root = BinaryTreeUtil.build_tree([1,2,3,4,5,6,7,8,9,10,11])
BinaryTreeUtil.pretty_print_tree(root)
Traverser().rev_level_order(root)