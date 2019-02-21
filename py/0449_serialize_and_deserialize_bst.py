"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, 
    or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. 
There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. 
Your serialize and deserialize algorithms should be stateless.
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode):
        """
        考虑按照 严格层序遍历 进行序列化
        """
        if not root:
            return ""
        serialization = ""
        level_queue = [root]
        while level_queue:
            temp_queue = []
            for node in level_queue:
                if node:
                    serialization += str(node.val) + ","
                    temp_queue.append(node.left)
                    temp_queue.append(node.right)
                else:
                    serialization += " " + ","
            level_queue = temp_queue
            serialization = serialization[:-1] + "#"
        serialization = serialization[:-1]

    def deserialize(self, data: str):
        if not data:
            return None
        levels = data.split("#")
        parent_queue = [TreeNode(int(levels[0]))]
        root = parent_queue[0]
        for level in levels[1:]:
            parent_queue = parent_queue[::-1]
            level = level.split(",")[::-1]
            temp_parent_queue = []
            while level:
                left = level.pop()
                right = level.pop()
                left = TreeNode(int(left)) if left != " " else None
                right = TreeNode(int(right)) if right != " " else None
                temp_parent_queue.append(left)
                temp_parent_queue.append(right)
                parent = parent_queue.pop()
                while not parent:
                    parent = parent_queue.pop()
                parent.left = left
                parent.right = right
            parent_queue = temp_parent_queue
        return root






# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
