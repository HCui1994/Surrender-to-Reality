class ListNode(object):
    def __init__(self, x, next=None):
        self.val, self.next = x, next


class SingleLinkedList(object):
    def __init__(self, nodes):
        self.head = self.build_linked_list(nodes)

    def build_linked_list(self, nodes: list):
        if not nodes:
            return None
        head = ListNode(nodes[0])
        curr = head
        for node in nodes[1:]:
            curr.next = ListNode(node)
            curr = curr.next
        return head

    def reverse_iterative(self):
        if not self.head or not self.head.next:
            return
        prev, curr = None, self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        self.head = prev

    def reverse_recursive(self):
        if not self.head or not self.head.next:
            return
        
        def reverse(head, new_head):
            if not head or not head.next:
                return head
            new_head = reverse(head.next, new_head)
            

    def traverse_linked_list(self):
        head = self.head
        buf = []
        while head:
            buf.append(head.val)
            head = head.next
        print(buf)


if __name__ == "__main__":
    single = SingleLinkedList([1, 2, 3, 4, 5, 6, 7])
    single.reverse_iterative()
    single.traverse_linked_list()
