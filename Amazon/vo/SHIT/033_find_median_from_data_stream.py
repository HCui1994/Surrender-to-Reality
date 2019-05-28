import heapq


class MedianFinder(object):

    def __init__(self):
        """
        always keep len(maxheap) - len(minheap) in {0, 1}
        """
        self.maxheap, self.minheap = []

    def addNum(self, num):
        if not self.maxheap:
            self.maxheap.append(-num)
            return
        if num <= -self.maxheap[0]:
            heapq.heappush(self.maxheap, -num)
            if (len(self.maxheap)) - len(self.minheap) not in {0, 1}:
                heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        else:
            heapq.heappush(self.minheap, num)
            if (len(self.maxheap)) - len(self.minheap) not in {0, 1}:
                heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

    def findMedian(self):
        if not self.maxheap:
            return None
        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] + self.minheap[0]) / 2.
        else:
            return -self.maxheap[0]
