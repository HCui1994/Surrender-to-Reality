"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.res = None
        self.k = k
        self.inorder(root, 0)
        self.counter = 0
        return self.res

    def inorder(self, node: TreeNode):
        if not node:
            return
        self.inorder(node.left)
        self.counter += 1
        if self.counter == self.k:
            self.res = node.val
            return
        self.inorder(node.right)

    def k_th_smallest_iterative(self, root, k):
        stack = [root]
        node = root
        counter = 0
        while stack and node:
            while node:
                node = node.left
                stack.append(node)
            node = stack.pop()
            if node:
                counter += 1
                if counter == k:
                    return node.val
            node = node.right

