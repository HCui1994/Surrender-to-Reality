
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Merger(object):
    def merge_k_lists(self, lists):
        import heapq
        dummy = ListNode("dummy")
        heap = []
        for i, head in enumerate(lists):
            heapq.heappush((head.val, i, head))
        node = dummy
        while heap:
            _, i, l = heapq.heappop(heap)
            node.next = l
            if l.next:
                heapq.heappush(heap, (l.next.val, i, l.next))
        return dummy.next
