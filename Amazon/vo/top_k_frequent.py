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

def main():
    soln = Solution()
    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k = 4
    soln.top_k_freq(words, k)


if __name__ == "__main__":
    main()