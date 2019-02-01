"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution(object):
    def subsets(self, nums):
        nums = tuple(nums)
        self.res = set()
        self.powerset(nums)
        print(self.res)

    def powerset(self, nums):
        print(nums)
        self.res.add(nums)
        for idx in range(1, len(nums)):
            self.powerset(nums[:idx])
            self.powerset(nums[idx:])

    def subsets2(self, nums):
        print(nums)
        if len(nums) == 0:
            return [[]]
        combs = self.subsets2(nums[1:])
        print(combs)
        return combs + [[nums[0]] + x for x in combs]


    def test(self):
        nums = [1,2,3]
        print(self.subsets2(nums))

Solution().test()
