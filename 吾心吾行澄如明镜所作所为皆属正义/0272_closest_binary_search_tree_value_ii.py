"""
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:

Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

Example:

Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

    4
   / \
  2   5
 / \
1   3

Output: [4,3]
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def closest_k_value(self, root, target, k):
        """
        bst的特性：中序遍历的结果即排序结果
        假设中序遍历的结果为 a1, a2, ..., an，与 target 最为接近的 k 个数一定是数列中连续的 k 个数
        维护一个长度为 k 的队列，
            1.  在中序遍历的过程中，每到一个节点，入队 distance
            2.  如果队列长度小于等于 k，继续
            3.  如果入队后队列长度大于 k，若新入队的 distance 小于等于队首 distance，队首 dequeue
                                      若新入队的 distance 大于队首 distance，pop 对尾 return
        """
        self.target = target
        self.k = k
        self.dist_queue = []
        self.val_queue = []
        self.inorder(root)
        return self.val_queue

    def inorder(self, node: TreeNode):
        if not node:
            return
        self.inorder(node.left)
        new_dist = abs(self.target - node.val)
        if len(self.dist_queue) <= self.k:
            self.dist_queue.append(new_dist)
            self.val_queue.append(node.val)
        else:
            if new_dist >= self.dist_queue[0]:
                self.dist_queue.pop()
                self.val_queue.pop()
                return
            else:
                self.dist_queue.pop(0)
                self.val_queue.pop(0)
        self.inorder(node.right)