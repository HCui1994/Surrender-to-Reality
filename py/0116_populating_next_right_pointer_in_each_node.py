"""
Given a binary tree
struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Note:
1.  You may only use constant extra space.
2.  Recursive approach is fine, implicit stack space does not count as extra space for this problem.
3.  You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).

Example:
Given the following perfect binary tree,
     1
   /  \
  2    3
 / \  / \
4  5  6  7

After calling your function, the tree should look like:
     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL
"""

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect_dict(self, root):
        """
        利用 perfect binary tree，将其视为 heap， 同时利用 heap 特性
        """
        pass

    def connect_bfs(self, root):
        """
        尝试 bfs 解决方案，但 bfs 需要额外空间，O(n/2)
        """
        if not root:
            return root
        queue = [root]
        counter = 1
        rightmost = 2
        prev = None
        while queue:
            curr = queue.pop(0)
            if counter == rightmost - 1:
                rightmost *= 2
                curr.next = None
                prev = None
            else:
                prev = curr
            if prev:
                prev.next = curr
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            counter += 1
        return root

    def connect_recursive(self, root):
        """
        对于每个节点，左子树最右侧与右子树最左侧的同层节点相连
        递归考虑每个节点
        """
        if not root:
            return None
        rightmost_on_left = root.left
        leftmost_on_right = root.right
        while rightmost_on_left and leftmost_on_right:
            rightmost_on_left.next = leftmost_on_right
            rightmost_on_left = rightmost_on_left.right
            leftmost_on_right = leftmost_on_right.left
        if root.left and root.right:
            self.connect_recursive(root.left)
            self.connect_recursive(root.right)
        # rightmost = root
        # while curr:
        #     rightmost.next = None
        #     rightmost = rightmost.right

            


    # def connect_perfect(self, root):
    #     if not root:
    #         return root
    #     prev = root
    #     curr = None
    #     while prev:
    #         prev_pointer = prev
    #         curr_pointer = curr
    #         while prev_pointer:
    #             if prev_pointer:
    #                 curr = prev_pointer.left
    #                 curr_pointer = curr
    #                 if prev_pointer.right:
    #                     curr_pointer.next = prev_pointer.right
    #                     curr_pointer = curr_pointer.next
    #                 break
    #             if prev_pointer.right:
    #                 curr = prev_pointer.right
    #                 curr_pointer = curr
    #                 break
    #             prev_pointer = prev_pointer.next



