import collections


class Solution(object):
    def subarrays_with_k_distinct(self, nums, k):
        counter = collections.Counter()
        left = right = 0
        while right < len(nums):
            counter[nums[right]] += 1
            if len(counter) < k:
                right += 1
                continue
            if len(counter) == k:
                left_backup = left

    def test(self):
        self.subarray([1, 2, 1, 2, 3], 2)


Solution().test()
