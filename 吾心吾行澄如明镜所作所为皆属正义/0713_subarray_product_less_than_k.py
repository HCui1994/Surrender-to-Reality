"""
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Note:
1.  0 < nums.length <= 50000.
2.  0 < nums[i] < 1000.
3.  0 <= k < 10^6.
"""


class Solution:
    def num_subarray_product_less_than_k_sliding_window(
            self, nums, k):
        """
        left 指针从 0 开始
        遍历 right，val 分别为 right 指针和 right 值
        """
        if k <= 1:
            return 0
        count = 0
        product = 1
        left = 0
        for right, val in enumerate(nums):
            product *= val
            # print(product)
            print("=====", left, right, product)
            while product >= k:
                print("+++++", left, right, product)
                product /= nums[left]
                left += 1
            # print(nums[left:right+1])
            count += right - left + 1
        print(count)
        return count

    def test(self):
        nums = [10, 5, 2, 6]
        k = 100
        self.num_subarray_product_less_than_k_sliding_window(nums, k)
        # self.num_subarray_product_less_than_k_sliding_window(nums, k)


Solution().test()
