"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL

Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotate_right(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head
        dummy = ListNode("dummy")
        dummy.next = head
        l = 0
        prev, curr = dummy, head
        while curr:
            l += 1
            prev = prev.next
            curr = curr.next

        k = k % l
        if k == 0:
            return head

        rightmost = prev

        j = l - k

        prev, curr = dummy, head
        while j > 0:
            curr = curr.next
            prev = prev.next
            j -= 1

        new_head = curr
        prev.next = None
        rightmost.next = head

        return new_head

    def rotate_right_2(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        curr = head
        curr = head.next
        prev = head
        l = 1
        while curr:
            curr = curr.next
            prev = prev.next
            l += 1
        print("shit")

        prev.next = head
        curr = head.next
        prev = head

    @staticmethod 
    def display(head: ListNode):
        curr = head
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        print(res)


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
head = ListNode("dummy")
curr = head
for e in l:
    curr.next = ListNode(e)
    curr = curr.next

head = head.next

Solution().rotate_right_2(head, 4)
Solution.display(head)
