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

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
Example:

Given the following binary tree,

     1
   /  \
  2    3
 / \    \
4   5    7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \    \
4-> 5 -> 7 -> NULL
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
    def connect_recursive(self, root):
        """
        与 116 同理，对于每个节点，如果同时有左子树和右子树，则在同一层中的，左子树的最右节点连接右子树最左节点
        WA! 
        """
        if not root or not root.left or not root.right:
            return root
        rightmost_on_left, leftmost_on_right = root.left, root.right
        while rightmost_on_left and leftmost_on_right:
            rightmost_on_left.next = leftmost_on_right
            if not rightmost_on_left.left and not rightmost_on_left.right:
                # 如果左子树到底
                continue
            if not leftmost_on_right.left and not leftmost_on_right.right:
                # 如果右子树到底
                continue
            if rightmost_on_left.right:
                # 先判断左子节点有没有右子树，使得左侧尽量向右沿伸
                rightmost_on_left = rightmost_on_left.right
            else:
                # 如果无法向右延伸，只好向左
                rightmost_on_left = rightmost_on_left.left  
            if leftmost_on_right.left:
                # 对右子同理
                leftmost_on_right = leftmost_on_right.left
            else:
                leftmost_on_right = leftmost_on_right.right
        if root.left:
            self.connect_recursive(root.left)
        if root.right:
            self.connect_recursive(root.right)

    def connect_recursive_with_extra_mem(self, root):
        if not root or not root.left or not root.right:
            return root
        memo = {}
        self._preorder_traverse(root, 0, memo)


    def _preorder_traverse(self, node, depth, memo):
        if memo.get(depth) is not None:
            memo[depth].next = node
            memo[depth] = node
        else:
            memo[depth] = node
        if not node.left and not node.right:
            return
        if node.left:
            self._preorder_traverse(node.left, depth + 1, memo)
        if node.right:
            self._preorder_traverse(node.right, depth + 1, memo)
        
    def connect_perfect(self, root):
        """
        bfs 算法，一层一层地对树进行遍历
        root: 指向上一层的第一个节点（parent level）
        tail: 指向下一层的最后一个节点（child level）
        parent level：可以视为一个链表，因为已经完成了遍历
        将所有可能的 tail 连起来
        """
        if not root:
            return

        sentinel = rear = TreeLinkNode(0)
        # enqueue root
        front = root
        front.next = rear

        while front is not rear:
            # dequeue from front
            node  = front
            front = front.next
            # if sentinel is dequeued
            if node is sentinel:
                # if rear has non sentinel items
                # enqueue sentinel back
                if rear is not sentinel:
                    rear.next = sentinel
                    rear = rear.next
                    continue

            if node.next is sentinel: # full level is traversed
                node.next = None

            # enqueue left
            if node.left:
                rear.next = node.left
                rear = rear.next
            # enqueue right
            if node.right:
                rear.next = node.right
                rear = rear.next