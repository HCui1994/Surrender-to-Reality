"""
We are given the root node of a maximum tree: a tree where every node has a value greater than any other value in its subtree.

Just as in the previous problem, the given tree was constructed from an list A (root = Construct(A)) recursively with the following Construct(A) routine:

If A is empty, return null.
Otherwise, let A[i] be the largest element of A.  Create a root node with value A[i].
The left child of root will be Construct([A[0], A[1], ..., A[i-1]])
The right child of root will be Construct([A[i+1], A[i+2], ..., A[A.length - 1]])
Return root.
Note that we were not given A directly, only a root node root = Construct(A).

Suppose B is a copy of A with the value val appended to it.  It is guaranteed that B has unique values.

Return Construct(B).

 

Example 1:
Input: root = [4,1,3,null,null,2], val = 5
Output: [5,4,null,1,3,null,null,2]
Explanation: A = [1,4,2,3], B = [1,4,2,3,5]

Example 2:
Input: root = [5,2,4,null,1], val = 3
Output: [5,2,4,null,1,null,3]
Explanation: A = [2,1,5,4], B = [2,1,5,4,3]

Example 3:
Input: root = [5,2,3,null,1], val = 4
Output: [5,2,4,null,1,3]
Explanation: A = [2,1,5,3], B = [2,1,5,3,4]
 
Note:
1 <= B.length <= 100
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = self.right = None

class Solution(object):
    def insert_into_max_tree(self, root, val):
        if not root:
            return TreeNode(val)
        if val > root.val:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        node = root
        while True:
            if val <= node.val:
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                if node.right:
                    if val <= node.right.val:
                        node = node.right
                        continue
                    else:
                        insert = TreeNode(val)
                        right_child = node.right
                        node.right, insert.left = insert, right_child
                        return root
        