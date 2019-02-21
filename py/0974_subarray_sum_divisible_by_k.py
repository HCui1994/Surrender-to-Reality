"""
Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

Example 1:
Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 
Note:
1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
"""


class Solution(object):
    def subarray_sum_div_by_k_cumulative_sum(self, nums, k):
        """
        累加和
        """
        count = 0
        length = len(nums)
        for i in range(length):
            if nums[i] == 0:
                count += 1
            cum_sum = 0
            for j in range(length):
                cum_sum += nums[j]
                if not cum_sum % k:
                    count += 1
        print(count)
        return count

    def subarray_sum_div_by_k_opt(self, nums, k):
        """
        LC560 subarray sum equals k
        """
        import collections
        count = 0
        remainder = 0
        memo = collections.Counter()
        memo[0] = 1 # memo 将在便利过程中，记录所有出现过的 sum(nums[0..i]) % k
        for num in nums:
            remainder = (remainder + num) % k # 当前累加和模 k 的余数 m = sum(nums[0..i]) mod k
            count += memo[remainder]
            memo[remainder] += 1
        print(count)
        return count

        

    def test(self):
        nums = [4, 5, 0, -2, -3, 1]
        k = 5
        self.subarray_sum_div_by_k_opt(nums, k)

Solution().test()
