class Solution(object):
    def max_sum(self, arr, k):
        if len(arr) < 3 * k:
            return []
        # init
        max_window_left = [-float("inf")] * (k - 1)
        cum_sum = [-float("inf")]
        summation = sum(arr[:k])
        max_window_left.append(summation)
        start, end = 1, k
        while end < len(arr):
            summation = summation + arr[end] - arr[start - 1]
            max_window_left.append(max(summation, max_window_left[-1]))
            cum_sum.append(summation)
            start += 1
            end += 1
        
            
        arr = arr[::-1]
        max_window_right = [-float("inf")] * (k - 1)
        summation = sum(arr[:k])
        max_window_right.append(summation)
        start, end = 1, k
        while end < len(arr):
            summation = summation + arr[end] - arr[start - 1]
            max_window_right.append(max(summation, max_window_right[-1]))
            start += 1
            end += 1
        max_window_right = max_window_right[::-1]
        
        arr = arr[::-1]
        window_mid = sum(arr[k: 2 * k - 1])

        print(max_window_left)
        print(max_window_right)
        print(cum_sum)

        window1_end, window2_start, window3_start = k - 1, k, len(arr) - k + 1
        


Solution().max_sum([1, 2, 1, 2, 6, 7, 5, 1], 2)
