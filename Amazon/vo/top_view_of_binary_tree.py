import sys
sys.path.append("../..")
from playground.TreePlayground import BinaryTreeUtil, TreeNode
import collections



class Viewer(object):
    def top_view_bt(self, root: TreeNode):
        # corner case:
        if not root:
            return []

        dq = collections.deque()
        dq.append((0, root))
        res_dict = {}
        while dq:
            x, node = dq.popleft()
            print(x, node)
            if x not in res_dict:
                res_dict[x] = node.val
            if node.left:
                dq.append((x - 1, node.left))
            if node.right:
                dq.append((x + 1, node.right))
        print(res_dict)


if __name__ == "__main__":
    root = BinaryTreeUtil.build_tree([1, 2, 3, 4, 5, 6, 7, 8, 9])
    BinaryTreeUtil.pretty_print_tree(root)
    viewer = Viewer()
    viewer.top_view_bt(root)
