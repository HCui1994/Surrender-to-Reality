class Traversal(object):
    def level_order(self, root):
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            level_queue = []
            level_res = []
            for node in queue:
                level_res.append(node.val)
                if node.left:
                    level_queue.append(node.left)
                if node.right:
                    level_queue.append(node.right)
            queue = level_queue
            res.append(level_res)
        return res
