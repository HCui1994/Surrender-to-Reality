"""
Given a list of non-negative numbers and a target integer k, 
    write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, 
    that is, sums up to n*k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
Note:
The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.

"""


class Solution(object):
    def check_subarray_sum_cummulative_summation(self, nums, k):
        for i in range(len(nums) - 1):
            summation = nums[i]
            for j in range(i + 1, len(nums)):
                summation += nums[j]
                if k == 0 and summation == 0:
                    return True
                if k == 0 and summation != 0:
                    continue
                if k != 0 and summation == 0:
                    return True
                if not summation % k:
                    return True
        return False

    def check_subarray_sum_set(self, nums, k):
        cum_sum_set = set()
        summation = 0
        for num in nums:
            summation += num
            prev_sum = summation - k

    def test(self):
        nums = [1, 2, 3]
        k = 0
        print(self.check_subarray_sum_cummulative_summation(nums, k))


Solution().test()