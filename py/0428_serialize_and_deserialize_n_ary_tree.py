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


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Codec(object):

    def serialize(self, root):
        serialization = str(self.inorder_helper(root))
        print(serialization)
        res = ""
        for symbol in serialization:
            if symbol != " " and symbol != ",":
                res += symbol
        return res

    def inorder_helper(self, node):
        if not node.children:
            return [node.val, []]
        return [node.val] + [self.inorder_helper(child) for child in node.children]
    
    def deserialize(self, data):
        if not data:
            return None
        scanner = 0
        dummy_head = Node("dummy head", [])
        stack = [dummy_head]
        val_stack = ["#"]
        root = None
        while scanner < len(data):
            # print(val_stack)
            # print(data[scanner:])
            # print("===")
            if data[scanner] == '[':
                # 如果遇到左括号，准备入栈
                scanner += 1
                if data[scanner] == ']':
                    scanner += 1
            elif data[scanner] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                val = ""
                while data[scanner] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    val += data[scanner]
                    scanner += 1
                val = int(val)
                node = Node(val, [])
                stack[-1].children.append(node)
                stack.append(node)
                val_stack.append(node.val)
            else:
                root = stack.pop()
                val_stack.pop()
                scanner += 1
        return root