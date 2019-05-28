class StreamKLargest(object):
    def __init__(self, k, nums, *args, **kwargs):
        self.k = k
        self.nums = nums
        self.minheap = []
        for val in nums:
            self.kth_largest(val)
                
        return super().__init__(*args, **kwargs)

    def add(self, val):
        import heapq
        if len(self.minheap) < self.k:
            heapq.heappush(self.minheap, val)
            return -1 if len(self.minheap) < self.k else self.minheap[0]
        if val > self.minheap[0]:
            heapq.heappop(self.minheap)
            heapq.heappush(self.minheap, val)
            return self.minheap[0]
        return self.minheap[0]