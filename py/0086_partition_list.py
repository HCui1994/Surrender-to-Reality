"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:
            return head

        dummy1 = ListNode("dummy1")
        dummy2 = ListNode("dummy2")
        curr, curr1, curr2 = head, dummy1, dummy2
        while curr:
            print(curr.val, curr.next)
            if curr.val < x:
                curr1.next = curr
                curr1 = curr1.next
            else:
                curr2.next = curr
                curr2 = curr2.next
            curr = curr.next
            print(curr)
        curr1.next = dummy2.next    # concat two linked lists
        curr2.next = None           # set tail
        # display_linked_list(dummy1.next)
        # display_linked_list(dummy2)
        return dummy1.next


def build_linked_list(arr: []) -> ListNode:
    if not arr:
        return None
    dummy_head = ListNode("dummy head")
    curr = dummy_head
    for e in arr:
        curr.next = ListNode(e)
        curr = curr.next

    return dummy_head.next


def display_linked_list(head: ListNode):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    print(arr)


head = build_linked_list([5, 3])
display_linked_list(head)

Solution().partition(head, 4)
