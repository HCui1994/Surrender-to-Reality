class TreeNode(object):
    def __init__(self, val, *args, **kwargs):
        self.val = val
        self.left = self.right = None
        return super().__init__(*args, **kwargs)

class Solution(object):
    def vertical_sum(self, root):
        import collections
        self.leftmost = self.rightmost = 0
        self.res_dict = collections.Counter()
        self.traverse(root, 0)
        res = []
        for x in range(self.leftmost, self.rightmost + 1):
            res.append(self.res_dict[x])
        print(res)
        
    def traverse(self, node, x):
        if not node:
            return 
        self.res_dict[x] += node.val
        self.leftmost = min(self.leftmost, x)
        self.rightmost = max(self.rightmost, x)
        self.traverse(node.left, x - 1)
        self.traverse(node.right, x + 1)



if __name__ == "__main__":
    import sys
    sys.path.append("../../")
    from playground.TreePlayground import BinaryTreeUtil
    root = BinaryTreeUtil.build_tree([3, 9, 8, 4, 0, 1, 7])
    soln = Solution()
    soln.vertical_sum(root)
    BinaryTreeUtil.pretty_print_tree(root)
