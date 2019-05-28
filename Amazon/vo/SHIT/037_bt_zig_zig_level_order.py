import sys
sys.path.append("../../..")
from playground.TreePlayground import BinaryTreeUtil, TreeNode


class BinaryTreeUtil(object):
    def zig_zag_level_order(self, root: TreeNode):
        import collections
        # corner case
        if not root:
            return []
        # init
        res = []
        queue = collections.deque()
        queue.append(root)
        l2r = True
        while queue:
            l2r = not l2r
            level_queue = collections.deque()
            level_res = []
            while queue:
                if not l2r:
                    node = level_queue.pop()
                    level_res.append(node.val)
                    if node.right:
                        level_queue.appendleft(node.right)
                    if node.left:
                        level_queue.appendleft(node.left)
                else:
                    node = level_queue.popleft()
                    level_res.append(node.val)
                    if node.left:
                        level_queue.append(node.left)
                    if node.right:
                        level_queue.append(node.right)
            queue = level_queue
            res.append(level_res)
    
        return res

