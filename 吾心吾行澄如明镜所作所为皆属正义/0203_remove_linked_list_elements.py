"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def remove_elements(self, head, val):
        if not head:
            return head
        pre_head = ListNode("pre_head")
        pre_head.next = head
        curr = pre_head
        while curr and curr.next:
            while curr.next and curr.next.val == val:
                curr.next = curr.next.next
            if curr.next:
                curr = curr.next
            else:
                break
            
        return pre_head.next