"""
Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverse_between(self, head : ListNode, m, n):
        if not head.next or m == n:
            return head
        pre_head = ListNode("pre_head")
        pre_head.next = head
        position = 1
        curr = head
        prev = pre_head
        while position < m:
            prev = curr
            curr = curr.next
            position += 1
        tail = None
        def _reverse(head, counter):
            if counter == n - m + 1:
                tail = head.next
                head.next = None
            if not head.next:
                return head
            new_head = _reverse(head.next, counter+1)
            head.next.next = head.next
            head.next = None
        prev.next = _reverse(curr)
        curr.next = tail
        return pre_head.next

