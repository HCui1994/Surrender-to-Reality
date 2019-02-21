# Definition for a binary tree node.
# Warm up, 10-26-2018
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, x):
        self._root = TreeNode(x)
    
    def insert(self, x):
        node = TreeNode(x)
        parent = self._root
        found_position = False
        while not found_position:
            if x <= parent.val and parent.left is not None:
                parent = parent.left
            elif x <= parent.val and parent.left is None:
                parent.left = node
                found_position = True
            elif x > parent.val and parent.right is not None:
                parent = parent.right
            elif x > parent.val and parent.right is None:
                parent.right = node
                found_position = True
    
    def preorder(self, node="first call", depth=0):
        if node == "first call":
            node = self._root
        curr = node
        if curr is None:
            return
        else:
            print("|      " * depth + "+--" + str(node.val))
            self.preorder(node=curr.left, depth=depth+1)
            self.preorder(node=curr.right, depth=depth+1)

    def depth(self, node="first_call"):
        if node == "first_call":
            node = self._root
        if node.left is None and node.right is None:
            return 0
        elif node.left is None and node.right is not None:
            return self.depth(node.right) + 1
        elif node.left is not None and node.right is None:
            return self.depth(node.left) + 1
        else:
            return max(self.depth(node.left), self.depth(node.right)) + 1

    def serialize(self):
        depth = self.depth(self._root)
        serial = [None] * (2 ** (depth + 1) - 1)
        serial[0] = self._root.val
        self._serializer(node=self._root, parent_pos=0, serial=serial)
        return serial

    def _serializer(self, node, parent_pos, serial):
        if node.left is not None:
            serial[2*parent_pos+1] = node.left.val
            self._serializer(node.left, 2*parent_pos+1, serial)
        if node.right is not None:
            serial[2*parent_pos+2] = node.right.val
            self._serializer(node.right, 2*parent_pos+2, serial)

    def deserialize(self, serial):
        head = TreeNode(serial[0])
        self._deserializer(parent_node=head, parent_position=0, serial=serial)
        return head

    def _deserializer(self, parent_node, parent_position, serial):
        if serial[parent_position*2+1] is not None:
            parent_node.left = TreeNode(serial[parent_position*2+1])
            if parent_position * 2 + 1 < len(serial) // 2:
                self._deserializer(parent_node=parent_node.left, parent_position=parent_position*2+1, serial=serial)
        if serial[parent_position*2+2] is not None:
            parent_node.right = TreeNode(serial[parent_position*2+2])
            if parent_position * 2 + 2 < len(serial) // 2:
                self._deserializer(parent_node=parent_node.right, parent_position=parent_position*2+2, serial=serial)


    def serialize2(self, node="first_call"):
        if node == "first_call":
            node = self._root
        serial = []
        self._serializer2(node, serial)
        return serial


    def _serializer2(self, node, serial):
        serial.append(node.val)
        if node.left is not None:
            self._serializer2(node.left, serial)
        else:
            serial.append(None)
        if node.right is not None:
            self._serializer2(node.right, serial)
        else:
            serial.append(None)

    def deserialize2(self, serial):
        if not serial:
            return None
        serial = serial[::-1]
        head = TreeNode(serial[len(serial)-1])
        serial.pop()
        self._deserializer2(parent_node=head, serial=serial)
        return head

    def _deserializer2(self, parent_node, serial):
        if not serial:
            return
        position = len(serial) - 1
        if serial[position] is not None:
            parent_node.left = TreeNode(serial[position])
            serial.pop()
            self._deserializer2(parent_node=parent_node.left, serial=serial)
        else:
            serial.pop()

        position = len(serial) - 1
        if serial[position] is not None:
            parent_node.right = TreeNode(serial[position])
            serial.pop()
            self._deserializer2(parent_node=parent_node.right, serial=serial)
        else:
            serial.pop()



        
        


# Tree test

# serial = binary_tree.serialize()

# test case
# serial = [1,None ,2,None ,3,None ,4,None ,5,None ,6,None ,7,None ,8,None ,9,None ,10,None]
# obviously, it is not a heap, cannot use BinaryTree.serialize()

import random
binary_tree = BinaryTree(5)
list = list(range(10))
random.shuffle(list)
for element in list:
    binary_tree.insert(element)

binary_tree.preorder()
serial = binary_tree.serialize2()
print("serial = {}\nlength = {}".format(serial, len(serial)))
head = binary_tree.deserialize2(serial)

binary_tree.preorder(head)








# 0297 Solution
# 10-26-2018
# DO NOT USE THIS SOLUTION

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Codec:
#     def depth(self, node):
#         if node.left is None and node.right is None:
#             return 0
#         elif node.left is None and node.right is not None:
#             return self.depth(node.right) + 1
#         elif node.left is not None and node.right is None:
#             return self.depth(node.left) + 1
#         else:
#             return max(self.depth(node.left), self.depth(node.right)) + 1
        
#     def serialize(self, root):
#         if root is None:
#             return []
#         elif root.left is None and root.right is None:
#             return [root.val]
#         depth = self.depth(root)
#         serial = [None] * (2 ** (depth + 1) - 1)
#         serial[0] = root.val
#         self._serializer(node=root, parent_pos=0, serial=serial)
#         return serial

#     def _serializer(self, node, parent_pos, serial):
#         if node.left is not None:
#             serial[2*parent_pos+1] = node.left.val
#             self._serializer(node.left, 2*parent_pos+1, serial)
#         if node.right is not None:
#             serial[2*parent_pos+2] = node.right.val
#             self._serializer(node.right, 2*parent_pos+2, serial)
        

#     def deserialize(self, serial):
#         if not serial:
#             return None
#         elif len(serial) == 1:
#             return TreeNode(serial[0])
#         head = TreeNode(serial[0])
#         self._deserializer(parent_node=head, parent_position=0, serial=serial)
#         return head

#     def _deserializer(self, parent_node, parent_position, serial):
#         if serial[parent_position*2+1] is not None:
#             parent_node.left = TreeNode(serial[parent_position*2+1])
#             if parent_position * 2 + 1 < len(serial) // 2:
#                 self._deserializer(parent_node=parent_node.left, parent_position=parent_position*2+1, serial=serial)
#         if serial[parent_position*2+2] is not None:
#             parent_node.right = TreeNode(serial[parent_position*2+2])
#             if parent_position * 2 + 2 < len(serial) // 2:
#                 self._deserializer(parent_node=parent_node.right, parent_position=parent_position*2+2, serial=serial)
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))



# update 10-27-2018
# AC!
# very slow because too many list.pop(0)
# try to optimize
# class Codec:

#     def serialize(self, node):
#         serial = []
#         if node == None:
#             return serial
#         self._serializer2(node, serial)
#         return serial


#     def _serializer2(self, node, serial):
#         serial.append(node.val)
#         if node.left is not None:
#             self._serializer2(node.left, serial)
#         else:
#             serial.append(None)
#         if node.right is not None:
#             self._serializer2(node.right, serial)
#         else:
#             serial.append(None)

#     def deserialize(self, serial):
#         if not serial:
#             return None
#         head = TreeNode(serial[0])
#         serial.pop(0)
#         self._deserializer2(parent_node=head, serial=serial)
#         return head

#     def _deserializer2(self, parent_node, serial):
#         if not serial:
#             return
#         if serial[0] is not None:
#             parent_node.left = TreeNode(serial[0])
#             serial.pop(0)
#             self._deserializer2(parent_node=parent_node.left, serial=serial)
#         else:
#             serial.pop(0)
#         if serial[0] is not None:
#             parent_node.right = TreeNode(serial[0])
#             serial.pop(0)
#             self._deserializer2(parent_node=parent_node.right, serial=serial)
#         else:
#             serial.pop(0)


# modified, mushc faster
class Codec:
    def serialize(self, node):
        serial = []
        if node == None:
            return serial
        self._serializer2(node, serial)
        return serial


    def _serializer2(self, node, serial):
        serial.append(node.val)
        if node.left is not None:
            self._serializer2(node.left, serial)
        else:
            serial.append(None)
        if node.right is not None:
            self._serializer2(node.right, serial)
        else:
            serial.append(None)

    def deserialize(self, serial):
        if not serial:
            return None
        serial = serial[::-1]
        head = TreeNode(serial[len(serial)-1])
        serial.pop()
        self._deserializer2(parent_node=head, serial=serial)
        return head

    def _deserializer2(self, parent_node, serial):
        if not serial:
            return
        position = len(serial) - 1
        if serial[position] is not None:
            parent_node.left = TreeNode(serial[position])
            serial.pop()
            self._deserializer2(parent_node=parent_node.left, serial=serial)
        else:
            serial.pop()

        position = len(serial) - 1
        if serial[position] is not None:
            parent_node.right = TreeNode(serial[position])
            serial.pop()
            self._deserializer2(parent_node=parent_node.right, serial=serial)
        else:
            serial.pop()