"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.

Follow up:
Could you do this in one pass?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def remove_nth_from_end_recursive(self, head, n):
        """
        递归方法其实也是 two pass
        """
        if not head or not head.next:
            return None
        dummy_head = ListNode("dummy")
        dummy_head.next = head
        self._recursive(dummy_head, head, head.next, n)
        return dummy_head.next

    def _recursive(self, prec, curr, succ, n):
        if not succ:
            if n == 1:
                prec.next = None
            return 1
        else:
            depth = self._recursive(curr, succ, succ.next, n) + 1
            if depth == n:
                prec.next = succ
            return depth

    def remove_nth_from_end_one_pass(self, head, n):
        """
        双指针 one pass 方法
        第一个指针领先第二个 n 个 node
        """
        ptr_1 = ptr_2 = head
        skip = 0
        while skip < n:
            ptr_1 = ptr_1.next
            skip += 1

        dummy_head = ListNode("dummy_head")
        prev = dummy_head
        while ptr_2:
            ptr_1 = ptr_1.next
            ptr_2 = ptr_2.next
            prev = prev.next
        prev.next = ptr_2.next
        return dummy_head.next
