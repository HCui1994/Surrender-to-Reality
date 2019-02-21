"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.

Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
import collections


class Solution(object):
    def four_sum(self, nums, target):
        """
        TLE
        """
        nums.sort()
        nums_counter = collections.Counter(nums)
        print(nums, nums_counter)
        length = len(nums)
        res = []
        for ai in range(length - 3):
            if ai > 0 and nums[ai] == nums[ai - 1]:
                continue
            for bi in range(ai + 1, length - 2):
                if bi > ai + 1 and nums[bi] == nums[bi - 1]:
                    continue
                for ci in range(bi + 1, length - 1):
                    if ci > bi + 1 and nums[ci] == nums[ci - 1]:
                        continue
                    # 在保证了 a b c 每次不一样的情况下，且对数列进行了排序，可以保证 d 不一样
                    # 以此达到去重的效果吗？
                    a, b, c = nums[ai], nums[bi], nums[ci]
                    d = target - a - b - c
                    if d not in nums_counter:
                        continue
                    if d < c:
                        continue
                    if d == c and collections.Counter([a, b, c, d])[d] > nums_counter[d]:
                        continue
                    res.append([a, b, c, d])
        return res

    def four_sum_general(self, nums, target):
        return self.n_sum(nums, target, 4)

    def n_sum(self, nums, target, n):
        def find_n_sum(left, right, target, n, result, results):
            # print(left, right, target, n, result, results)
            if right - left + 1 < n or n < 2 or target < nums[left] * n or target > nums[right] * n:
                return
            if n == 2:
                # 递归出口：2_sum 作为最小子问题
                while left < right:
                    sub_target = nums[left] + nums[right]
                    if sub_target < target:
                        left += 1
                    elif sub_target > target:
                        right -= 1
                    else:
                        results.append(result + [nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left] - 1:
                            left += 1
                        while right > left and nums[right] == nums[right] + 1:
                            right += 1
            else:
                for i in range(left, right + 1, +1):
                    # if i > left and nums[i] == nums[i - 1]:
                    #     continue
                    if i == left or (i > left and nums[i-1] != nums[i]):
                        find_n_sum(left=i + 1,
                                right=right,
                                target=target - nums[i],
                                n=n - 1,
                                result=result + [nums[i]],
                                results=results)

        nums.sort()
        results = []
        find_n_sum(0, len(nums) - 1, target, n, [], results)
        return results

    def test(self):
        nums = [-1, 0, -5, -2, -2, -4, 0, 1, -2]
        target = -9
        print(self.four_sum_general(nums, target))


Solution().test()
