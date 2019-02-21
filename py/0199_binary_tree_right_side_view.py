"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def right_side_view(self, root : TreeNode):
        """
        第一印象是要建立左孩子右兄弟，所有 right side view 节点即为左孩子右兄弟表示法的叶节点。但是！是错误的！

        每一层只有一个节点在结果集合中，该节点为前序遍历该层中最后一个访问到的节点
        建立一个dict，每次刷新每层见到的节点
        """
        if not root:
            return []
        right_side_view_dict = {0: root}
        if root.left:
            self._preorder_traverse(root.left, 1, right_side_view_dict)
        if root.right:
            self._preorder_traverse(root.right, 1, right_side_view_dict)
        res = []
        for _, node in right_side_view_dict.items():
            res.append(node)
        return res

    def _preorder_traverse(self, node : TreeNode, depth, right_side_view_dict):
        print(right_side_view_dict)
        right_side_view_dict[depth] = node
        if not node.left and not node.right:
            return
        if node.left:
            self._preorder_traverse(node.left, depth + 1, right_side_view_dict)
        if node.right:
            self._preorder_traverse(node.right, depth + 1, right_side_view_dict)
