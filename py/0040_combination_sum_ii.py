"""
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
    [1, 7],
    [1, 2, 5],
    [2, 6],
    [1, 1, 6]
]
Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
    [1,2,2],
    [5]
]
"""

import collections


class Solution(object):
    def combination_sum_2(self, candidates, target):
        counter = collections.Counter(candidates)
        self.target = target
        self.res = set()
        self.helper(counter, [], 0)
        return list(self.res)

    def helper(self, counter, temp_res, temp_sum):
        print(temp_res, temp_sum)
        if temp_sum > self.target:
            return
        if temp_sum == self.target:
            self.res.add(tuple(sorted(temp_res)))
        for num in counter:
            if counter[num] == 0:
                continue
            counter[num] -= 1
            self.helper(counter, temp_res + [num], temp_sum + num)
            counter[num] += 1

    def combination_sum_speed_boost(self, candidates, target):
        self.target = target
        self.candidates = sorted(candidates)
        self.res = []
        self.helper2(0, 0, [])
        return list(self.res)

    def helper2(self, idx, prev_sum, prev_res):
        if prev_sum > self.target:
            return
        if prev_sum == self.target:
            self.res.append(prev_res)
        start_idx = idx
        while idx < len(self.candidates):
            if idx > start_idx and self.candidates[idx] == self.candidates[idx - 1]:
                idx += 1
                continue
            self.helper2(idx + 1, prev_sum + self.candidates[idx], prev_res + [self.candidates[idx], ])
            idx += 1

    def test(self):
        print(self.combination_sum_speed_boost([10, 1, 2, 7, 6, 1, 5], 8))


Solution().test()
