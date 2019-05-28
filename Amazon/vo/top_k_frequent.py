import collections
import heapq


class MaxHeapObj(tuple):
    def __init__(self, val, *args, **kwargs):
        self.val = val
        return super().__init__(*args, **kwargs)

    def __lt__(self, other):
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val

    def __str__(self):
        return str(self.val)


class Solution(object):
    def top_k_freq(self, words, k):
        # corner case
        if not words:
            return []
        if k > len(words):
            return sorted(words)
        # preprocess
        counter = collections.Counter(words)  # count frequency
        # count top k words
        maxheap = []
        for word, freq in counter.items():
            heapq.heappush(maxheap, MaxHeapObj((-freq, word)))
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        # collecct result
        res = []
        while maxheap:
            # maintain sequence
            res.append(heapq.heappop(maxheap)[1])
        return res[::-1]


# Time complexity analysis:  n <=> total num of words
# preprocess: O(n)   go through all words
# counting: O(n log k) --  heappush all words * log (heap_size)
# collect result: O(log k)
# Total class: O(n log k)

# Space complexity
# counter: O(m)  m <=> num of diff words
# heap: O(k)
# Total class: O(max(k, m))


class MaxHeap(list):
    def __init__(self, data=[], *args, **kwargs):
        super().__init__(data, *args, **kwargs)
        self.heapify()

    def heapify(self):
        if not self:
            return
        for pos in reversed(range(len(self) // 2)):
            self._sinkdown(pos)

    def _sinkdown(self, pos):
        while pos * 2 + 1 < len(self):
            # current node has (left) child
            if pos * 2 + 2 >= len(self):
                # no right chile
                maxchild = pos * 2 + 1
            else:
                if self[pos * 2 + 1] > self[pos * 2 + 2]:
                    maxchild = pos * 2 + 1
                else:
                    maxchild = pos * 2 + 2
            if self[pos] < self[maxchild]:
                self[pos], self[maxchild] = self[maxchild], self[pos]
                pos = maxchild
                continue
            break

    def _floatup(self, pos):
        parentpos = (pos - 1) // 2
        while parentpos >= 0:
            # current node has parent
            if self[pos] >= self[parentpos]:
                self[pos], self[parentpos] = self[parentpos], self[pos]
                pos, parentpos = parentpos, (parentpos - 1) // 2
                continue
            break

    def heappush(self, item):
        self.append(item)
        pos = len(self) - 1
        self._floatup(pos)

    def heappop(self):
        if not self:
            return None
        self[0], self[-1] = self[-1], self[0]
        ret = self.pop()
        self._sinkdown(0)
        return ret


class TopK(object):
    def top_k_freq(self, words, k):
        import collections
        if len(words) <= k:
            return words
        counter = collections.Counter(words)
        # heap = MaxHeap([(-freq, num) for num, freq in counter.items()])
        heap = MaxHeap()
        for word, freq in counter.items():
            heap.heappush((-freq, word))
            print(heap)
            if len(heap) > k:
                heap.heappop()
        res = []
        print("shit")
        while heap:
            print(heap)
            res.append(heap.heappop()[1])
        print(res[::-1])


def main():
    soln = TopK()
    words = [5, 3, 1, 1, 1, 3, 5, 73, 1]
    k = 3
    soln.top_k_freq(words, k)


if __name__ == "__main__":
    main()
