from playground.LinkedListPlayground import SingleLinkedListUtil, SingleListNode
import sys
sys.path.append("../..")


class MinHeapObj(SingleListNode):
    def __eq__(self, other):
        return self.val == other.val

    def __ne__(self, other):
        return self.val != other.val

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val

    def __le__(self, other):
        return self.val <= other.val

    def __ge__(self, other):
        return self.val >= other.val


class Heap(object):
    def __init__(self, heap, *args, **kwargs):
        self.heap = heap
        self._heapify()
        return super().__init__(*args, **kwargs)

    def __str__(self):
        res = []
        for item in self.heap:
            res.append(item.val)
        return str(res)

    def __len__(self):
        return len(self.heap)

    def __getitem__(self, key):
        return self.heap[key].val if key < len(self) else None

    def __setitem__(self, key, val):
        if key >= len(self):
            return None
        self[key].val = val

    def _floatup(self, pos):
        parent_pos = (pos - 1) // 2
        while parent_pos >= 0:
            if self[pos] < self[parent_pos]:
                self[pos], self[parent_pos] = self[parent_pos], self[pos]
                pos = parent_pos
                continue
            break

    def _sinkdown(self, pos):
        while pos * 2 + 1 < len(self):  # current ele has child
            if pos * 2 + 2 >= len(self):
                minchild_pos = pos * 2 + 1
            else:
                if self[pos * 2 + 1] < self[pos * 2 + 2]:
                    minchild_pos = pos * 2 + 1
                else:
                    minchild_pos = pos * 2 + 2
            if self[pos] >= self[minchild_pos]:
                self[pos], self[minchild_pos] = self[minchild_pos], self[pos]
                pos = minchild_pos
                continue
            break

    def _heapify(self):
        for pos in reversed(range(len(self) // 2)):
            self._sinkdown(pos)

    def heappush(self, val):
        self.heap.append(val)
        self._floatup(len(self) - 1)

    def heappop(self):
        self[0], self[-1] = self[-1], self[0]
        val = self.heap.pop()


class Solution(object):
    def merge_two_sorted_linked_list(self, l1, l2):
        dummy = SingleListNode("dummy")
        node = dummy
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        if not l1:
            node.next = l2
        else:
            node.next = l1
        return dummy.next

    def merge_tow_unsorted_linked_list(self, l1, l2):
        dummy = SingleListNode("dummy")
        heap = []
        node = l1
        while node:
            heap.append(MinHeapObj(node))
            node = node.next
        print(heap)


if __name__ == "__main__":
    l1 = SingleLinkedListUtil.build_linked_list([1, 3, 5, 7, 9])
    l2 = SingleLinkedListUtil.build_linked_list([2, 4, 6, 8])
    soln = Solution()
    head = soln.merge_tow_unsorted_linked_list(l1, l2)
    # SingleLinkedListUtil.print_single_linked_list(head)
