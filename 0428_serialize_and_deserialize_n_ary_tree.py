"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, 
    or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. 

There is no restriction on how your serialization/deserialization algorithm should work. 

You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following 3-ary tree as [1 [3[5 6] 2 4]]. 

You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note:
1.  N is in the range of [1, 1000]
2.  Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Codec(object):

    def serialize(self, root: Node):
        if not root:
            return ""
        level_queue = [[root]]
        serialization = ""
        while level_queue:
            temp_level_queue = []
            for children in level_queue:
                for child in children:
                    serialization += str(child.val) + '|'
                    if child.children:
                        temp_level_queue.append(child.children)
            level_queue = temp_level_queue
        print(serialization)



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
