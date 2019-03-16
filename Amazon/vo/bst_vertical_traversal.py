import collections


class TreeNode(object):
    def __init__(self, x, *args, **kwargs):
        self.val = x
        self.left = self.right = None
        return super().__init__(*args, **kwargs)


class Solution(object):
    def bst_vertical(self, root: TreeNode):
        # corner case: root is empty
        if not root:
            return []
        # init
        leftmost = rightmost = 0    # border, for faster go through
        res_dict = collections.defaultdict(list)   # hashmap, vertical cordinate as ke
        dq = collections.deque()    # bst queue
        dq.append([0, root])        # root at origin x = 0
        # bsf
        while dq:
            x, node = dq.popleft()
            leftmost = min(leftmost, x)
            rightmost = max(rightmost, x)  # refresh border
            res_dict[x].append(node.val)
            if node.left:
                dq.append([x - 1, node.left])
            if node.right:
                dq.append([x + 1, node.right])
        # collect results according to vertical order
        res = []
        for x in range(leftmost, rightmost + 1):
            res.append(res_dict[x])
        return res
