class TreeNode(object):
    def __init__(self, x, *args, **kwargs):
        self.val = x
        self.left = self.right = None
        return super().__init__(*args, **kwargs)


class BinarySearchTree(object):
    def __init__(self, values=None, *args, **kwargs):
        self.root = self.build_bst(values)
        return super().__init__(*args, **kwargs)

    def build_bst(self, values):
        if not values:
            return None
        root = TreeNode(values[0])
        left, right = [], []
        for val in values[1:]:
            if val < values[0]:
                left.append(val)
            else:
                right.append(val)
        root.left = self.build_bst(left)
        root.right = self.build_bst(right)
        return root

    def insert(self, x):
        if not self.root:
            self.root = TreeNode(x)
            return
        node = self.root
        while node:
            # print(type(node), node)
            parent = node
            if x < node.val:
                node = node.left
                is_left = True
            else:
                node = node.right
                is_left = False
        if is_left:
            parent.left = TreeNode(x)
        else:
            parent.right = TreeNode(x)

    def search_closest(self, val):
        if not self.root:
            return None
        
        node = self.root
        min_diff = abs(val - node.val)
        closest_candidate = node
        while node:
            if node.val == val:
                return val
            diff = abs(val - node.val)
            if diff < min_diff:
                min_diff = diff
                closest_candidate = node
            if val < node.val:
                node = node.left
            else:
                node = node.right
        return closest_candidate.val

    def search_upperbound(self, val):
        if not self.root:
            return None

        node = self.root
        min_diff = float("inf") if val > node.val else node.val - val
        upperbound_candidate = None if val > node.val else node
        while node:
            if node.val == val:
                return val
            if val > node.val:
                node = node.right
            else:
                diff = node.val - val
                if diff < min_diff:
                    min_diff = diff
                    upperbound_candidate = node
                node = node.left
        return upperbound_candidate.val if min_diff != float("inf") else None

    def search_lowerbound(self, val):
        if not self.root:
            return None
        node = self.root
        min_diff = float("inf") if val < node.val else val - node.val
        lowerbound_candidate = None if val < node.val else node
        while node:
            if node.val == val:
                return val
            if node.val < val:
                diff = val - node.val
                if diff < min_diff:
                    min_diff = diff
                    lowerbound_candidate = node
                node = node.right
            else:
                node = node.left

        if lowerbound_candidate:
            return lowerbound_candidate.val
        else:
            return None
                
                


if __name__ == "__main__":
    import sys
    sys.path.append("../..")
    from playground.TreePlayground import BinaryTreeUtil
    bst = BinarySearchTree([5, 2, 7, 3, 9, 1, 6, 4, 8])
    bst.insert(999)
    bst.insert(998)
    closest = bst.search_lowerbound(23893)
    print(closest)
    # BinaryTreeUtil.pretty_print_tree(bst.root)
