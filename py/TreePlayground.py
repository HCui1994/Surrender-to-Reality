class TreePlayground(object):
    def inorder(self, root):
        res = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left    
            root = stack.pop()
            res.append(root.val)
            root = root.right

    def preorder(self, root):
        res = []
        stack = []
        while stack or root:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left    
            root = stack.pop()
            root = root.right
    
    def postorder(self, root):
        res = []
        stack = [root]
        while stack:
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
            res.append(root.val)
            root = stack.pop()
        


