"""
Given an array  of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
import collections

class Solution(object):
    def three_sum_closest_counter(self, nums, k):
        """
        按照 3 sum 的思路，先将 nums 排序，三数之和为 0，必然有正有负
        但是本题中，k 值不定，可以全正，也可以全负
        """
        length = len(nums)
        if length < 3:
            return 0
        if length == 3:
            return sum(nums)
        # nums.sort()
        nums_counter = collections.Counter(nums)
        nums_deduplicate = list(nums_counter.keys())
        a_plus_b_dict = {}
        for a in nums_deduplicate:
            for b in nums_deduplicate:
                if a == b and nums_counter[a] < 2:
                    # 如果 a == b，但是没有两个重复的数，跳过
                    continue
                # 注意，不要这样交换
                # 这实际上是对数组按下标访问
                # 对数组中的值访问，access by reference, 如果交换会使得数组变换，导致 bug
                # if a > b:
                #     a, b = b, a
                if (a + b) not in a_plus_b_dict.keys():
                    a_plus_b_dict[a + b] = set([(min(a, b), max(a, b))])
                else:
                    a_plus_b_dict[a + b].add((a, b))
        
        res = nums[0] + nums[1] + nums[2]
        min_diff = float("inf")
        for c in [0,1]:
            print(c, min_diff)
            for a_plus_b, ab_set in a_plus_b_dict.items():
                if abs(k - a_plus_b - c) < min_diff:
                    for a, b in ab_set:
                        if a != b and a != c and b != c:
                            print("==1")
                            res = a_plus_b + c
                            min_diff = min(min_diff, abs(k - a_plus_b - c))
                        elif a == b and b != c and nums_counter[a] >= 2:
                            print("==2")
                            res = a_plus_b + c
                            min_diff = min(min_diff, abs(k - a_plus_b - c))
                        elif a != b and b == c and nums_counter[b] >= 2:
                            print(a, b, c)
                            print("==3")
                            res = a_plus_b + c
                            min_diff = min(min_diff, abs(k - a_plus_b - c))
                        elif a == c and b != c and nums_counter[c] >= 2:
                            print("==4")
                            res = a_plus_b + c
                            min_diff = min(min_diff, abs(k - a_plus_b - c))
                        elif a == b and b == c and nums_counter[a] >= 3:
                            print("==5")
                            res = a_plus_b + c
                            min_diff = min(min_diff, abs(k - a_plus_b - c))
        return res

    def three_sum_closest_two_pointers(self, nums, k):
        pass


    def test(self):
        nums = [1, 1, 1, 0]
        k = 100
        print(self.three_sum_closest_counter(nums, k))



Solution().test()