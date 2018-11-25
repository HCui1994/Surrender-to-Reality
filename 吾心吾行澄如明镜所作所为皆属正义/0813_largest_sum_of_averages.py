"""
We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum of the average of each group. 
What is the largest score we can achieve?

Note that our partition must use every number in A, and that scores are not necessarily integers.

Example:
Input: 
A = [9,1,2,3,9]
K = 3
Output: 20
Explanation: 
The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned A into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.

Note:

1.  1 <= A.length <= 100.
2.  1 <= A[i] <= 10000.
3.  1 <= K <= A.length.
Answers within 10^-6 of the correct answer will be accepted as correct.
"""

class Solution:
    def largest_sum_of_averages_recursion(self, nums, k):
        """ 
        每个数字都有 k 种选择 
        先考虑递归解法
        """
        group = [[] for _ in range(k)]
        return self._dfs(nums, 0, group)

    def _dfs(self, nums, idx, group):
        if idx == len(nums):
            sum_avg = 0
            for k in range(len(group)):
                if len(group[k]) == 0:
                    return 0
                else:
                    sum_avg += sum(group[k]) / len(group[k])
            return sum_avg
        num = nums[idx]
        brach_sums = []
        for k in range(len(group)):
            group[k].append(num)
            brach_sums.append(self._dfs(nums, idx + 1, group))
            group[k].pop()
        return max(brach_sums)

    def largest_sum_of_averages_recursion_with_memoization(self, nums, k):
        """
        如何在递归基础上增加备忘以减少运算量？
        """
        memo = {}
        group = [[] for _ in range(k)]
        return self._dfs_2(nums, 0, group, memo)

    def _calc_key(self, nums):
        key = 0
        for num in nums:
            key = key * 10 + num
        return key

    def _dfs_2(self, nums, idx, group, memo):
        if idx == len(nums):
            sum_avg = 0
            for k in range(len(group)):
                if len(group[k]) == 0:
                    return 0
                else:
                    sum_avg += sum(group[k]) / len(group[k])
            print("========", sum_avg)
            return sum_avg
        key = self._calc_key(nums[idx:])
        if key in memo.keys():
            print('shit')
            print(memo)
            return memo[key]
        num = nums[idx]
        brach_sums = []
        for k in range(len(group)):
            group[k].append(num)
            brach_sums.append(self._dfs_2(nums, idx + 1, group, memo))
            group[k].pop()
        if max(brach_sums) != 0:
            memo[key] = max(brach_sums)
        return memo[key]

    def largest_sum_of_averages_dp(self, nums, k):
        """ 
        Backpack ??!! 
        """
        #  memo[i][k] 表示将 nums[:i] 分入 k 组时的最大得分.
        memo = []

    def test(self):
        nums = [9,1,2,3,9]
        k = 3
        ans = self.largest_sum_of_averages_recursion_with_memoization(nums, k)
        print(ans)


soln = Solution()
soln.test()