"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:
Search for a node to remove.
If the node is found, delete the node.

Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def delete_node(self, root: TreeNode, key):
        """
        在找到了需要删除的节点时，考虑
        case1：要删除的节点是叶节点，直接删除 
        case2：要删除的节点有左子树，没有又子树，将左子树提升到当前节点位置（需要记录parent）
        case3：要删除的节点有右子树，没有左子树，同理
        case4：要删除的节点既有左子树，也有右子树，删除节点后，将左子树整体插入右子树中（或反之）
        """
        if not root:
            return None
        dummy_head = TreeNode("dummy head")
        parent = dummy_head
        parent.right = root
        node_to_delete = None
        if root.val == key:
            is_found = True
            node_to_delete = root
        curr = root
        while True:
            if not curr:
                break
            if key == curr.val:
                node_to_delete = curr
                break
            elif key < curr.val:
                parent = curr
                curr = curr.left
            else:
                parent = curr
                curr = curr.right
        if node_to_delete:
            is_left = node_to_delete == parent.left
            if not node_to_delete.left and not node_to_delete.right:
                if is_left:
                    parent.left = None
                else:
                    parent.right = None
            elif node_to_delete.left and not node_to_delete.right:
                if is_left:
                    parent.left = node_to_delete.left
                else:
                    parent.right = node_to_delete.left
            elif not node_to_delete.left and node_to_delete.right:
                if is_left:
                    parent.left = node_to_delete.right
                else:
                    parent.right = node_to_delete.right
            else:
                sub_tree_left = node_to_delete.left
                sub_tree_right = node_to_delete.right
                if is_left:
                    parent.left = sub_tree_left
                else:
                    parent.right = sub_tree_left
                to_insert = sub_tree_left
                while to_insert.right:
                    to_insert = to_insert.right
                to_insert.right = sub_tree_right
        return dummy_head.right
                
                
