"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generate_trees(self, n):
        return self.build_bst(1, n + 1)

    def build_bst(self, left, right):
        if left == right:
            return [None]
        bst = []
        for i in range(left, right):
            left_trees = self.build_bst(left, i)
            right_trees = self.build_bst(i + 1, right)
            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    bst.append(root)
        return bst

    def test(self):
        n = 1
        self.generate_trees(n)


Solution().test()
