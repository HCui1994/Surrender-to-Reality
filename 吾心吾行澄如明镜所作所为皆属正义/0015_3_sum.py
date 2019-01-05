"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution(object):
    def three_sum(self, nums):
        """
        三个数必定有正有负，可以先将数组排序，以此来去重
        TLE

        mgj，想死
        """
        nums = sorted(nums)
        if len(nums) < 3 or nums[0] > 0 or nums[-1] < 0:
            return []
        length = len(nums)
        ci_start = 2
        res = set()
        print(nums)
        # case 1: a, b <= 0, c > 0
        a_plus_b_dict = {}
        for ai in range(length - 2):
            if nums[ai] > 0:
                # c 从第一个正数开始找
                ci_start = ai
                break
            for bi in range(ai + 1, length - 1):
                if nums[bi] > 0:
                    break
                a_plus_b = nums[ai] + nums[bi]
                if a_plus_b not in a_plus_b_dict.keys():
                    a_plus_b_dict[a_plus_b] = set([(ai, bi)])
                else:
                    a_plus_b_dict[a_plus_b].add((ai, bi))
        for ci in range(ci_start, length):
            if nums[ci] <= 0:
                # 如果 c 不是正数，跳过
                continue
            if -nums[ci] in a_plus_b_dict.keys():
                for ai, bi in a_plus_b_dict[-nums[ci]]:
                    res.add((nums[ai], nums[bi], nums[ci]))

        # case 2: a, b >= 0, c < 0
        nums = nums[::-1]
        a_plus_b_dict = {}
        for ai in range(length - 2):
            if nums[ai] < 0:
                ci_start = ai
                break
            for bi in range(ai + 1, length - 1):
                if nums[bi] < 0:
                    break
                a_plus_b = nums[ai] + nums[bi]
                if a_plus_b not in a_plus_b_dict.keys():
                    a_plus_b_dict[a_plus_b] = set([(ai, bi)])
                else:
                    a_plus_b_dict[a_plus_b].add((ai, bi))
        for ci in range(ci_start, length):
            if nums[ci] >= 0:
                continue
            if -nums[ci] in a_plus_b_dict.keys():
                for ai, bi in a_plus_b_dict[-nums[ci]]:
                    res.add((nums[ci], nums[bi], nums[ai]))

        for i in range(length - 2):
            if (nums[i], nums[i + 1], nums[i + 2]) == (0, 0, 0):
                res.add((0, 0, 0))

        return list(res)

    def three_sums_two_counter(self, nums):
        import collections
        res = set()
        nums = sorted(nums)
        if not nums or nums[0] > 0 or nums[-1] < 0:
            return []
        nums_counter = collections.Counter(nums)
        nums_set = list(nums_counter.keys())[::-1]
        print(nums_set)
        # print(nums_counter)
        if nums_counter[0] >= 3:
            res.add((0, 0, 0))
        for a in nums:
            if a >= 0:
                break
            for c in nums_set:
                if c < 0:
                    break
                b = -(a + c)
                # print(a, b, c)
                if (a == b and nums_counter[a] > 1) or (b == c and nums_counter[c] > 1) or (nums_counter[b] > 0 and a != b and b != c):
                    # print("1===", a, b, c)
                    res.add(tuple(sorted([a, b, c])))
        return list(res)

    # def three_sum_two_pointers(self, nums):
    #     nums.sort()
    #     N, result = len(nums), []
    #     if N < 3:
    #         return result
    #     for i in range(N - 2):
    #         if i > 0 and nums[i] == nums[i - 1]:
    #             continue
    #         target = -nums[i]  # 遍历数列，从 0 到 n - 2，将当前数字作为第一个数字
    #         left = i + 1  # 当前数字的后一个作为 left
    #         right = N - 1   # 数列的最后一个数字作为 right
    #                         # 在数列 nums[left .. right] 中寻找剩下的两个数
    #         while left < right:
    #             twoSum = nums[left] + nums[right]
    #             if twoSum > target:
    #                 # 如果 left + right 比 target 要大，说明，算多了，要减少
    #                 right -= 1
    #             elif twoSum < target:
    #                 # 如果比 target 要小，说明算少了，要增加
    #                 left += 1
    #             else:
    #                 result.append([nums[i], nums[left], nums[right]])
    #                 left += 1
    #                 right -= 1
    #                 while left < N and nums[left-1] == nums[left]:
    #                     # 手动去重，如果下一个 left 和当前 left 相等，left 继续向右侧推进
    #                     left += 1
    #                 while right > 0 and nums[right+1] == nums[right]:
    #                     # right 同理
    #                     right -= 1
    #     return result

    def three_sum_two_pointers(self, nums):
        nums.sort()
        if len(nums) < 3 or nums[0] > 0 or nums[-1] < 0:
            return []
        length = len(nums)
        res = []
        for ai in range(length - 2):
            if ai > 0 and nums[ai] == nums[ai - 1]:
                continue
            a = nums[ai]
            b_plus_c = 0 - a
            bi, ci = ai + 1, length - 1
            while bi < ci:
                b, c = nums[bi], nums[ci]
                if b + c < b_plus_c:
                    bi += 1
                elif b + c > b_plus_c:
                    ci -= 1
                else:
                    res.append([a, b, c])
                    bi, ci = bi + 1, ci - 1
                    while bi < length - 1 and nums[bi] == nums[bi - 1]:
                        bi += 1
                    while ci > 2 and nums[ci] == nums[ci + 1]:
                        ci -= 1
        return res

    def test(self):
        nums = [-1, -1, -1, -1, -3, -2, -2, 0, 0, 0, 0, 0, 4]
        print(self.three_sum_two_pointers(nums))


Solution().test()
