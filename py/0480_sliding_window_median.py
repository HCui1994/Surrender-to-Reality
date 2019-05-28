"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position. 
our job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note: 
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.
"""


class Stream(object):
    def __init__(self, *args, **kwargs):
        self.maxheap, self.minheap = [], []

    def income(self, val):
        import heapq
        # push heap
        if not self.maxheap:
            heapq.heappush(self.maxheap, -val)
            return val
        if val > -self.maxheap[0]:
            heapq.heappush(self.minheap, val)
        else:
            heapq.heappush(self.maxheap, -val)
        # rebalance
        if len(self.maxheap) - len(self.minheap) == 2:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        elif len(self.maxheap) - len(self.minheap) == -1:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
        # return median
        if len(self.maxheap) - len(self.minheap) == 1:
            return -self.maxheap[0]
        else:
            return (-self.maxheap[0] + self.minheap[0]) / 2.


class Solution(object):
    def median_sliding_window(self, nums: [int], k: int) -> [float]:
        import collections
        # corner case
        if len(nums) < k:
            return None
        if len(nums) == k:
            return sum(nums)
        # init
        res = []
        summation = sum(nums[:k])
        print(nums, sum(nums[:k]))
        stream = Stream()
        res.append(stream.income(summation))
        end = 1 + k
        while end <= len(nums):
            print(summation)
            start = end - k
            summation -= nums[start - 1]
            summation += nums[end - 1]
            res.append(stream.income(summation))
            end += 1
        print(res)


Solution().median_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3)
