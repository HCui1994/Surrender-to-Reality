"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

import collections
import heapq


class Solution(object):
    def top_k_frequent(self, nums, k):
        counter = collections.Counter(nums)
        counter = [(-value, key) for key, value in counter.items()]
        heapq.heapify(counter)
        res = []
        while counter and k > 0:
            res.append(heapq.heappop(counter)[1])
            k -= 1
        # print(res)
        return res


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    soln = Solution()
    soln.top_k_frequent(nums, k)
