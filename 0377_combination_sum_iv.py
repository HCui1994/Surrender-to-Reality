"""
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.
Example: 
nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers? 
"""

class Solution:
    def combination_sum_4_recursion(self, nums, target):
        """ 
        为了遍历所有的情况，首先想到的应该是 dfs 
        """
        if not nums:
            return 0
        return self._dfs(nums, target)

    def _dfs(self, nums, remaining_target):
        if remaining_target == 0:
            return 1
        if remaining_target < 0:
            return 0
        return sum([self._dfs(nums, remaining_target - num) for num in nums])

    def combination_sum_4_recursion_with_memoization(self, nums, target):
        """
        如何能够通过 memoization 减少运算量？
        AC, but still slow, only beats 1.2%
        """
        if not nums:
            return 0
        memo = {}
        return self._dfs_2(nums, target, memo)

    def _dfs_2(self, nums, remaining_target, memo):
        if remaining_target == 0:
            return 1
        if remaining_target < 0:
            return 0
        if remaining_target in memo.keys():
            print("shit")
            return memo[remaining_target]
        memo[remaining_target] = sum([self._dfs_2(nums, remaining_target - num, memo) for num in nums])
        return memo[remaining_target]


    def combination_sum_4_dp(self, nums, target):
        """ dp 能不能快一点？ """
        if not nums:
            return 0
        # memo[i] 表示 target == 1 时，有多少种方法
        memo = [None for _ in range(target + 1)]
        memo[0] = 


    def test(self):
        nums = [1, 2, 3]
        target = 4
        ans = self.combination_sum_4_recursion_with_memoization(nums, target)
        print(ans)


soln = Solution()
soln.test()
