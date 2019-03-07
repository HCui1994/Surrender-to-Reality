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
    def reverse_between(self, head, m, n):
        counter = 1
        dummy_head = ListNode("dummy")
        dummy_head.next = head
        prev, node = dummy_head, head
        while counter < m:
            prev, node = node, node.next
            counter += 1
        start = node
        
        while counter < n + 1:
            node = node.next
            counter += 1
        end = node
        print(start, end)
        prev.next = self.reverse(start, end)
        return dummy_head.next

    def reverse(self, start, end):
        prev, curr = None, start
        while curr != end:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        start.next = end
        return prev

    def display(self, head):
        if not head:
            print("empty")
            return
        node = head
        while node:
            print(node.val, " -> " if node.next else "", end="")
            node = node.next
        print("")

    def build_linkedlist(self, nodes):
        dummy_head = ListNode("dummy")
        curr = dummy_head
        for node in nodes:
            curr.next = ListNode(node)
            curr = curr.next
        return dummy_head.next


if __name__ == "__main__":
    soln = Solution()
    head = soln.build_linkedlist([2, 5])
    soln.display(head)
    head = soln.reverse_between(head, 1, 2)
    soln.display(head)