"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""

# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        非递归中序遍历，需要 stack 大小为 O(h)
        """
        self._stack = []
        self._node = root
        if self._node or self._stack:
            while self._node:
                self._stack.append(self._node)
                self._node = self._node.left
        
    def hasNext(self):
        if self._node or self._stack:
            return True
        else:
            return False
        
    def next(self):
        if self._node or self._stack:
            while self._node:
                self._stack.append(self._node)
                self._node = self._node.left
            self._node = self._stack.pop()
            res = self._node.val
            self._node = self._node.right
            return res

    def _build_BST_preorder(self, preorder):
        root = TreeNode(preorder[0])
        for idx in range(1, len(preorder)):
            node = TreeNode(preorder[idx])
            curr = parent = root
            while curr:
                parent = curr
                if node.val < parent.val:
                    curr = curr.left
                else:
                    curr = curr.right
            if node.val < parent.val:
                parent.left = node
            else:
                parent.right = node
        return root
    
    def _inorder_recursive(self, root):
        if root.left:
            self._inorder_traverse(root.left)
        print(root.val)
        if root.right:
            self._inorder_traverse(root.right)

    def _inorder_iterative(self, root):
        stack = []
        node = root
        while node or stack:
            # print(node.val)
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            print(node.val)   # ////////// visit 在外层循环，内层循环之后
            node = node.right

    def _preorder_recursive(self, root):
        print(root.val)
        if root.left:
            self._preorder_recursive(root.left)
        if root.right:
            self._preorder_recursive(root.right)
    
    def _preorder_iterative(self, root):
        stack = []
        node = root
        while node or stack:
            while node:
                print(node.val)   # /////////// visit 在内层循环
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right

    def _postorder_recursive(self, root):
        if root.left:
            self._postorder_recursive(root.left)
        if root.right:
            self._postorder_recursive(root.right)
        print(root.val)
    
    def _postorder_iterative(self, root):
        stack = [root]
        stack_visit = []
        node = root
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            stack_visit.append(node)
        while stack_visit:
            print(stack_visit.pop().val)
            



    def test(self):
        root = self._build_BST_preorder([5,1,4,2,3,9,7,6,8])
        self._postorder_recursive(root)
        print("====")
        self._postorder_iterative(root)


BSTIterator(None).test()


        




# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())