class SlidingMax(object):
    def sliding_window_max(self, arr, k):
        import collections
        if len(arr) < k:
            return []
        dq = collections.deque()
        res = []
        for i, num in enumerate(arr):
            if dq and i - dq[0] >= k:
                dq.popleft()
            while dq and num > arr[dq[0]]:
                dq.popleft()
            dq.append(i)
            if i >= k - 1:
                res.append(arr[dq[0]])
        print(res)


SlidingMax().sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], k=3)
