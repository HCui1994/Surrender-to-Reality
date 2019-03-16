class Solution:
    def largestSumAfterKNegations(self, arr, k):
        import heapq
        pos_heap = []
        neg_heap = []
        for item in arr:
            if item < 0:
                heapq.heappush(neg_heap, item)
            else:
                heapq.heappush(pos_heap, item)
        while k and neg_heap:
            heapq.heappush(pos_heap, -heapq.heappop(neg_heap))
            k -= 1
        while k:
            pos_heap[0] *= -1
            k -= 1
        return (sum(pos_heap) + sum(neg_heap))


soln = Solution()
soln.largestSumAfterKNegations([3, -1, 0, 2],  3)
