"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note: 
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
"""


class Solution(object):
    def max_sliding_window(self, nums, k):
        import collections
        if not nums or not k:
            return []
        res = []
        dq = collections.deque([])
        for i in range(len(nums)):
            if dq and dq[0] == i - k:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            print(dq)
            if i >= k - 1:
                res = nums[dq[0]]
        # print(res)
        return res

    def test(self):
        # nums = [142, 38, 100, 53, 22, 84, 168, 50, 194, 136, 111, 13, 47, 45, 151, 164, 126, 47, 106, 124, 183, 8, 87, 38, 91, 121, 102, 46, 82, 195, 53, 18, 11, 165, 61]
        # k = 35
        self.max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3)


Solution().test()
