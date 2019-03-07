class TreeeNode(object):
    def __init__(self, x, *args, **kwargs):
        self.val = x
        self.left = self.right = None
        return super().__init__(*args, **kwargs)


def insert(root, val):
    if not root:
        root = TreeeNode(val)
        return root
    dummy_parent = TreeeNode(float("inf"))
    dummy_parent.left = root
    parent, node = dummy_parent, root
    is_left = True
    while node:
        if val < node.val:
            parent, node = node, node.left
            is_left = True
        else:
            parent, node = node, node.right
            is_left = False
    if is_left:
        parent.left = TreeeNode(val)
    else:
        parent.right = TreeeNode(val)
    return root

def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)
    

root = None
for val in [12, 10, 15, 19, 20]:
    root = insert(root, val)


def bst_upperbound(root, val):
    if not root:
        return None
    node = root
    candidate = float("inf")
    while node:
        if val == node.val:
            return val
        if val > node.val:
            node = node.right
            continue
        if val < node.val:
            candidate = min(candidate, node.val)
            node = node.left
            continue
    if candidate == float("inf"):
        return None
    return candidate

def bst_lower_bound(root, val):
    if not root:
        return None
    node = root
    candidate = -float("inf")
    while node:
        if val == node.val:
            return val
        if val > node.val:
            candidate = max(candidate, node.val)
            node = node.right
            continue
        if val < node.val:
            node = node.left
            continue
    if candidate == float("inf"):
        return None
    return candidate

def bst_clostest(root, val):
    if not root:
        return None
    node = root
    candidate = node.val
    min_diff = abs(candidate - val)
    while node:
        if node.val == val:
            return val
        if abs(node.val - val) < min_diff:
            candidate = node.val
            min_diff = abs(node.val - val)
        if val < node.val:
            node = node.left
        else:
            node = node.right
    return candidate
        
        


print(bst_upperbound(root, 16))
print(bst_lower_bound(root, 16))
print(bst_clostest(root, 999))