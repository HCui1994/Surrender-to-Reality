"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
import heapq


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def merge_k_lists(self, lists: list[ListNode]):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        dummy_head = ListNode("dummy head")
        pq = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(pq, (l.val, i, l))
        node = dummy_head
        while pq:
            _, i, l = heapq.heappop(pq)
            node.next = l
            node = node.next
            if l.next:
                pq.heappush(pq, (l.next.val, i, l.next))
        return dummy_head.next
            