"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. 
If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Follow up:
Can you solve it without using extra space?
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def delete_cycle(self, head: ListNode):
        """
        LC 0287 鸽巢原理证明，快慢双指针
        """
        slow = fast = head
        if not head or not head.next or not head.next.next:
            return None

        while True:
            if not fast:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # slow fast 指针有可能同时停在head 处
                # 即整个链表的入口即是环入口。此时fast恰好绕了环两圈，slow 恰好绕了患一圈
                break
        finder = head
        while True:
            if slow == finder:
                # 不同于 LC0287，由于 head 即可能为环入口，所以需要在 slow finder 指针向后移动之前判断是否相等
                break
            slow = slow.next
            finder = finder.next

        return finder
