"""
Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.
In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)
Return the number of moves required to make every node have exactly one coin.
"""


class Solution:
    def distribute_coins(self, root):
        self.moves = 0
        return self.distributer(root)

    def distributer(self, node):
        """
        如果不管当前节点是什么，在向上返回的时候，都会扣留一个硬币
        剩下的硬币，不管是盈余还是亏欠，都要继续向上返回
        每到一个节点，计算子树中需要的移动次数，不管盈余还是亏钱，都需要累加
        """
        if not node:
            return 0
        left_lacks = self.distributer(node.left)
        right_lacks = self.distributer(node.right)
        self.moves += abs(left_lacks) + abs(right_lacks)
        return node.val - 1 + (left_lacks + right_lacks)

        