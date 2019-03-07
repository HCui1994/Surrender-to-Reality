class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverse_nodes_in_k_group(self, head, k):
        dummy_head = ListNode("dummy")
        dummy_head.next = head
        prev, start, end = dummy_head, head, head
        while True:
            cnt = 0
            while cnt < k and end:
                end = end.next
                cnt += 1
            if cnt == k:
                period_head = self.reverse(start, end)
                prev.next = period_head
                start.next = end
                prev, start = start, start.next
            else:
                break
        return dummy_head.next

    def reverse(self, start, end="default"):
        print(start.val, end.val if end else "#")
        if end == "default":
            end = None
        curr, prev = start, None
        while curr != end:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
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
    linked_list = soln.build_linkedlist([1, 2, 3, 4, 5, 6, 7, 8, 9])
    soln.display(linked_list)
    linked_list = soln.reverse_nodes_in_k_group(linked_list, 4)
    soln.display(linked_list)
