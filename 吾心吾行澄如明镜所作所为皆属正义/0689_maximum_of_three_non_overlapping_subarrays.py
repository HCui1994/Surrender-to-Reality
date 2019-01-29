"""
In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). 
If there are multiple answers, return the lexicographically smallest one.

Example:
Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.

Note:
nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).
"""


class Solution(object):
    def max_sum_of_three_subarrays_brutal(self, nums, k):
        """
        预处理：计算 k-累加和数组
        遍历 k-累加和数列，找到下标 m, n, p 的三个数，使得相加最大
        且满足：p - n >= k, n - m > k

        TLE
        """
        cum_sum = [0]
        k_cum_sum = []
        summation = 0
        for idx, num in enumerate(nums):
            summation += num
            cum_sum.append(summation)
            if idx < k - 1:
                continue
            k_cum_sum.append(summation - cum_sum[idx - (k - 1)])
        k_cum_sum_len = len(k_cum_sum)
        max_sum = 0
        res = (0, k, k * 2)
        for m in range(k_cum_sum_len - k):
            for n in range(m + k, k_cum_sum_len - 1):
                for p in range(n + k, k_cum_sum_len):
                    if k_cum_sum[m] + k_cum_sum[n] + k_cum_sum[p] > max_sum:
                        max_sum = k_cum_sum[m] + k_cum_sum[n] + k_cum_sum[p]
                        res = (m, n, p)
        print(res)
        return res

    def max_sum_of_three_subarrays_(self, nums, k):
        """
        与暴力方法同理，先创建k-累加和数列，并找到下表为 m, n, p 的三个数，使得三个数的和最大，且下标满足 p - n >= k, n - m > k
        假设对于一个给定的数列，k = 3
        已经求得k-累加和数列
        s0 s1 s2 s3 s4 s5 s6 s7 s8 s9
                    n
        假设 n = 4，则 m 一定在 n - k = 1 之前（包含3）
                      p 一定在 n + k = 7 之后 （包含7）
        可以对k-累加和数列在此进行遍历，计算 x 之前，之后出现过的最大值
        """
        cum_sum = [0]
        k_cum_sum = []
        summation = 0
        for idx, num in enumerate(nums):
            summation += num
            cum_sum.append(summation)
            if idx < k - 1:
                continue
            k_cum_sum.append(summation - cum_sum[idx - (k - 1)])
        k_cum_sum_len = len(k_cum_sum)
        max_before_idx = {0: (k_cum_sum[0], 0)}
        max_after_idx = {k_cum_sum_len - 1: (k_cum_sum[-1], k_cum_sum_len - 1)}
        for idx in range(1, k_cum_sum_len):
            if k_cum_sum[idx] > max_before_idx[idx - 1][0]:
                max_before_idx[idx] = (k_cum_sum[idx], idx)
            else:
                max_before_idx[idx] = max_before_idx[idx - 1]
        for idx in range(k_cum_sum_len - 2, -1, -1):
            if k_cum_sum[idx] >= max_after_idx[idx + 1][0]:
                max_after_idx[idx] = (k_cum_sum[idx], idx)
            else:
                max_after_idx[idx] = max_after_idx[idx + 1]
        max_sum = 0
        # print(k_cum_sum)
        # print(max_before_idx)
        # print(max_after_idx)
        for n in range(k, k_cum_sum_len - k):
            m, p = n - k, n + k
            if max_before_idx[m][0] + k_cum_sum[n] + max_after_idx[p][0] > max_sum:
                max_sum = max_before_idx[m][0] + k_cum_sum[n] + max_after_idx[p][0]
                res = (max_before_idx[m][1], n, max_after_idx[p][1])
        # print(res)
        return res


        


    def test(self):
        print(self.max_sum_of_three_subarrays_([1, 2, 1, 2, 6, 7, 5, 1], 2))



Solution().test()
