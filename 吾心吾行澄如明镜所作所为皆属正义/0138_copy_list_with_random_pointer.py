"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
Return a deep copy of the list.

SCORE: 
1930 -> 1946
1 attempt (re)
100%
"""

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copy_random_list(self, head : RandomListNode):
        """
        建立由旧节点向拷贝节点的映射
        """
        # 注意初始化，防止 random 指针指向 None
        node_dict = {None: None}
        curr = head
        # print(head)
        while curr:
            node_dict[curr] = RandomListNode(-curr.label)
            curr = curr.next
        # print(head)
        # print(node_dict)
        curr = head
        while curr:
            # print(curr, curr.next, curr.random)
            node_dict[curr].next = node_dict[curr.next]
            node_dict[curr].random = node_dict[curr.random]
            curr = curr.next
        return node_dict[head]
    
    def _build_list(self, list):
        if not list:
            return None
        head = RandomListNode(list[0])
        curr = head
        for l in list[1:]:
            curr.next = RandomListNode(l)
            curr = curr.next
        return head
    
    def _traverse(self, head):
        while head:
            print(head.label)
            head = head.next

    def test(self):
        head = self._build_list([1,2])
        # self._traverse(head)
        self._traverse(self.copy_random_list(head))



Solution().test()