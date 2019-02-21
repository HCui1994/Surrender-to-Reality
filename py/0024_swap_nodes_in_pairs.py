"""
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swap_pairs(self, head : ListNode):
        if not head or not head.next:
            return head
        new_head = ListNode("head")
        prev, curr, succ = new_head, head, head.next
        shit = head
        # print(str(prev)[-3:], str(curr)[-3:], str(succ)[-3:], str(succ.next)[-3:], str(succ.next.next)[-3:])
        while True:
            prev.next = succ
            post_succ = succ.next
            succ.next = curr
            curr.next = post_succ
            # print("+++", str(prev.next)[-3:], str(curr.next)[-3:], str(succ.next)[-3:])
            if not post_succ or not post_succ.next:
                break
            else:
                # 采用这种 确定一个引用，向后顺延 的方式不容易出错
                prev = prev.next.next
                curr, succ = prev.next, prev.next.next
            # print(str(prev)[-3:], str(curr)[-3:], str(succ)[-3:])
        return new_head.next


    def swap_pairs_recursive(self, head : ListNode):
        if not head or not head.next:
            return head
        new_head = ListNode("head")
        prev, curr, succ = new_head, head, head.next
        self._swapper(prev, curr, succ)
        return new_head.next

    def _swapper(self, prev : ListNode, curr : ListNode, succ : ListNode):
        post_succ = succ.next
        prev.next = succ
        curr.next = post_succ
        succ.next = curr
        prev = prev.next.next
        if not prev.next or not prev.next.next:
            return
        curr, succ = prev.next, prev.next.next
        self._swapper(prev, curr, succ)
        