"""
Median is the middle value in an ordered integer list. 
If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3
[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 
Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2

Follow up:
If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
"""

import heapq


class MedianFinder(object):
    def __init__(self):
        self.minheap, self.maxheap = [], []

    def add_num(self, num):
        if not self.maxheap:
            # 如果整个数据结构是空的
            self.maxheap.append(-num)
            return
        if num <= -self.maxheap[0]:
            # 新加入的数字在较小的一侧
            heapq.heappush(self.maxheap, -num)
            if len(self.maxheap) - len(self.minheap) > 1:
                # 如果较小的一侧比较大的一侧多了两个，则需要 rearrange
                heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        else:
            heapq.heappush(self.minheap, num)
            if len(self.minheap) - len(self.maxheap) > 0:
                # 如果较大的一侧比较小的一侧多，则需要 rearrage
                heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

    def find_median(self):
        if not self.maxheap:
            return None
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        else:
            return (-self.maxheap[0] + self.minheap[0]) / 2.

    def display(self):
        print(self.maxheap, self.minheap)


def test():
    mf = None
    op_flow = ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
               "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian"]
    pa_flow = [[], [6], [], [10], [], [2], [], [6], [], [5], [], [0], [], [6], [], [3], [], [1], [], [0], [], [0], []]
    for op, param in zip(op_flow, pa_flow):
        if op == "MedianFinder":
            mf = MedianFinder()
        elif op == "addNum":
            mf.add_num(param[0])
            mf.display()
        elif op == "findMedian":
            print(mf.find_median())
            mf.display()


if __name__ == "__main__":
    test()
