"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
    find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution(object):
    def combination_sum(self, candidates, target):
        self.target = target
        self.res = []
        self.helper(0, [], candidates)
        return self.res

    def helper(self, prev_sum, prev_res, candidates):
        if prev_sum == self.target:
            self.res.append(prev_res)
            return
        for idx, candidate in enumerate(candidates):
            if prev_sum + candidate > self.target:
                continue
            self.helper(prev_sum + candidate, prev_res + [candidate], candidates[idx:])

    def test(self):
        candidates = [1, 2, 3]
        target = -1
        print(self.combination_sum(candidates, target))


Solution().test()
