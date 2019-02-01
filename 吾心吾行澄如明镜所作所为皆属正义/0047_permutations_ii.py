"""
 Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution(object):
    def permute_unique_recursive(self, nums):
        self.res = set()
        self.helper([], nums)
        print(list(self.res))

    def helper(self, res, nums):
        if not nums:
            self.res.add(tuple(res))
            return
        for idx in range(len(nums)):
            self.helper(res + [nums[idx]], nums[:idx] + nums[idx + 1:])

    def permute_unique_iterative(self, nums):
        res = []
        fact = lambda x: 1 if x == 0 or x == 1 else x * fact(x - 1)
        for _ in range(fact(len(nums))):
            res.append(self.next_permute(nums).copy())
            if len(res) > 1 and res[-1] == res[-2]:
                res.pop()
        print(res)
        return res
            

    def next_permute(self, permute):
        carry_position = len(permute) - 2
        while permute[carry_position] >= permute[carry_position + 1]:
            carry_position -= 1
        # print(permute[carry_position])
        if carry_position == -1:
            return permute[::-1]
        switch_position = len(permute) - 1
        while permute[switch_position] <= permute[carry_position]:
            switch_position -= 1
        permute[switch_position], permute[carry_position] = permute[carry_position], permute[switch_position]
        permute[carry_position + 1:] = permute[carry_position + 1:][::-1]
        return permute.copy()

    def test(self):
        nums = [1,1,2]
        self.permute_unique_iterative(nums)


Solution().test()
