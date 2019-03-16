class SingleListNode(object):
    def __init__(self, x, next=None):
        self.val, self.next = x, next


class SingleLinkedListUtil(object):

    @staticmethod
    def build_linked_list(nodes: list):
        if not nodes:
            return None
        head = SingleListNode(nodes[0])
        curr = head
        for node in nodes[1:]:
            curr.next = SingleListNode(node)
            curr = curr.next
        return head

    @staticmethod
    def reverse_iterative(self, head):
        if not head or not head.next:
            return
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        head = prev
        return head

    @staticmethod
    def print_single_linked_list(head):
        buf = []
        while head:
            buf.append(head.val)
            head = head.next
        print(buf)


if __name__ == "__main__":
    single = SingleLinkedList([1, 2, 3, 4, 5, 6, 7])
    single.reverse_iterative()
    single.traverse_linked_list()
