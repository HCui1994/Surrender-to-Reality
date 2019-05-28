class SubarraySum(object):
    def maximum(self, arr):
        cummulate = [0]
        minsum = summation = 0
        maxsum = -float("inf")
        for num in arr:
            summation += num
            maxsum = max(maxsum, summation - minsum)
            minsum = min(minsum, summation)
            cummulate.append(summation)
        return maxsum
            
        


SubarraySum().maximum([-2, 1, -3, 4, -1, 2, 1, -5, 4],)
