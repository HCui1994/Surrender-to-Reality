"""
Given a singly linked list L: L(0) → L(1) → … → L(n-1) → L(n),
reorder it to: L(0) → L(n) → L(1) → L(n-1) → L(2) → L(n-2) → …

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:
Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorder_list(self, head):
        """
        使用 O(n) 的额外空间
        """
        if not head or not head.next or not head.next.next:
            return head
        node_list = []
        curr = head
        while curr:
            node_list.append(curr)
            curr = curr.next
        length = len(node_list)
        for idx in range(length // 2):
            node_list[idx].next = node_list[length - idx - 1]
            if length - idx - 1 > idx + 1:
                node_list[length - idx - 1].next = node_list[idx + 1]
        node_list[idx + 1].next = None


    def reorder_list_mem_opt(self, head):
        """
        不使用额外空间
        1. 将链表后一半反转
            1 2 3 4 5 6 7 8 -> 1 2 3 4 8 7 6 5
                               ^       ^
                               head    tail
        2. 按顺序重新创建链接
        """
        if not head or not head.next or not head.next.next:
            return
        length = 0
        curr = head
        tail = None
        while curr:
            length += 1
            tail = curr
            curr = curr.next
        skip_length = length // 2
        half_head = head
        for idx in range(skip_length):
            half_head = half_head.next
        if length % 2:
            half_head.next = self._reverse(half_head.next)
            half_head = half_head.next
        else:
            half_head = self._reverse(half_head)
        node1, node2 = head, half_head
        # return half_head
        for _ in range(length // 2):
            # print(node1.val, node2.val)
            node1_next, node2_next = node1.next, node2.next
            node1.next = node2
            node2.next = node1_next
            node1 = node1_next
            if not node2.next:
                node2 = None
            node2 = node2_next
            # print(node1.val, node2.val)
        print("shit")
        # return node2
        return head

    def _reverse(self, head):
        if not head or not head.next:
            return head
        new_head = self._reverse(head.next)
        head.next.next = head
        head.next = None
        return new_head




    def test(self):
        def build_list(input):
            dummyRoot = ListNode(0)
            ptr = dummyRoot
            for number in input:
                ptr.next = ListNode(number)
                ptr = ptr.next

            ptr = dummyRoot.next
            return ptr

        def print_linked_list(node):
            if not node:
                print("[]")
                return
            result = ""
            while node:
                result += str(node.val) + ", "
                node = node.next
            print("[" + result[:-2] + "]")
            
        nodes = [2,3,4,5]
        head = build_list(nodes) 
        head = self.reorder_list_mem_opt(head)
        print_linked_list(head)



Solution().test()
