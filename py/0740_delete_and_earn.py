"""
Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operations.

Example 1:
Input: nums = [3, 4, 2]
Output: 6
Explanation: 
Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points. 6 total points are earned.
Example 2:
Input: nums = [2, 2, 3, 3, 3, 4]
Output: 9
Explanation: 
Delete 3 to earn 3 points, deleting both 2's and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.
Note:

The length of nums is at most 20000.
Each element nums[i] is an integer in the range [1, 10000].
"""

class Solution:
    def delete_and_earn(self, nums):
        """
        类似于 house robber ii (0221)？
        每到一个数，都有两种选择
        1. collect，则不能收集所有比他大一和小一的数
        2. uncollect，则可以
        注意，一次删除就会删除所有
        """
        if len(nums) < 2:
            return sum(nums)
        nums_sorted = sorted(nums)
        nums_deduplicate = list(set(nums))
        nums_sorted += [0]
        summation = []
        tmp_sum = nums_sorted[0]
        for i in range(1, len(nums_sorted), +1):
            if nums_sorted[i] == nums_sorted[i - 1]:
                tmp_sum += nums_sorted[i]
            else:
                summation.append(tmp_sum)
                tmp_sum = nums_sorted[i]
        # print(nums_sorted)
        # print(nums_deduplicate)
        # print(summation)
        # memo[i] 表示，到 nums[i] 为止能收集到的最大总数
        memo = [[None, None] for _ in range(len(nums_deduplicate))]
        memo[0] = [summation[0], 0]
        for i in range(1, len(nums_deduplicate), +1):
            # 如果收集当前的数，就不能拿所有比它小 1 的数
            # 如果选择拿 x，就可以拿所有的 x
            # 因为一次删除就会去除所有 x-1, x+1 的数
            if nums_deduplicate[i] - nums_deduplicate[i - 1] == 1:
                # 如果当前的数比前一个数恰好大了 1，则会删除前一个数（即不能收集前一个数）
                collect = memo[i - 1][1] + summation[i]
            else:
                # 如果当前的数比前一个数大了不止 1，则 前一个数可以取，也可以不取
                collect = max(memo[i - 1]) + summation[i]
            # ######### 注意，这段代码是错误的！########
            # if nums_deduplicate[i] - nums_deduplicate[i - 1] == 1:
            #     # 如果当前的数比前一个数刚好大了 1，则必然必然会拿前一个数
            #     uncollect = memo[i - 1][0]
            # else:
            #     # 如果前一个数与当前数之差大于 1，就可能会拿，也可能不会拿
            #     uncollect = max(memo[i - 1])
            # ######################################
            uncollect = max(memo[i - 1])
            memo[i] = [collect, uncollect]
        print(memo)
        return max(memo[-1])
            

        


    def test(self):
        nums = [1,1,1,2,4,5,5,5,6]
        ans = self.delete_and_earn(nums)

soln = Solution()
soln.test()