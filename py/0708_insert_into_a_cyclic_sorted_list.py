"""
Given a node from a cyclic linked list which is sorted in ascending order, write a function to insert a value into the list such that it remains a cyclic sorted list. 
The given node can be a reference to any single node in the list, and may not be necessarily the smallest value in the cyclic list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the cyclic list should remain sorted.

If the list is empty (i.e., given node is null), you should create a new single cyclic list and return the reference to that single node. 
Otherwise, you should return the original given node.
"""

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'Node', insert_val: 'int') -> 'Node':
        if not head:
            head = Node(insert_val)
            head.next = head
            return head
        curr, next = head, head.next
        while curr != next:
            if curr.val <= insert_val <= next.val or curr.val > next.val >= insert_val or insert_val >= curr.val > next.val:
                break
            curr, next = curr.next, next.next
        curr.next = Node(insert_val, next)
        return curr