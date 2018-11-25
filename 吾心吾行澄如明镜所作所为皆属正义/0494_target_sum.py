"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. 
Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""

class Solution:
    def __init__(self):
        self.target = 0

    def target_sum_recursion(self, nums, target):
        """
        为每个数字创建 +/- 分支，以遍历所有情况
        TLE
        """
        self.target = target
        return self.dfs(nums, 0)

    def dfs(self, nums, prev_sum):
        # print(nums, prev_sum)
        if not nums:
            return prev_sum == self.target
        return self.dfs(nums[1:], prev_sum + nums[0]) + self.dfs(nums[1:], prev_sum - nums[0])

    def target_sum_recursion_with_memoization(self, nums, target):
        # memo[idx][tgt] 记录，前 idx 个数的和为 tgt，有多少种方法
        memo = [{} for _ in range(len(nums))]
        ans = self.dfs_2(nums, target, 0, memo)
        print(memo)
        return ans

    def dfs_2(self, nums, target, idx, memo):
        if idx == len(nums):
            # 如果使用了所有的数字，恰好完全消耗了 target，则是一个合法的解，返回 1，否则返回 0
            return target == 0
        if target in memo[idx].keys():
            # 如果之前已经计算过，当前 idx下，达到 target 值有多少种方法，直接返回
            return memo[idx][target]
        # 如果 nums[idx] 采用了加号，则剩余的 target -= nums[idx]
        add_branch = self.dfs_2(nums, target - nums[idx], idx + 1, memo)
        # 如果 nums[idx] 采用了减号，则剩余的 target += nums[idx]
        sub_branch = self.dfs_2(nums, target + nums[idx], idx + 1, memo)
        memo[idx][target] = add_branch + sub_branch
        return memo[idx][target]
        
    # def target_sum_dp_backpack(self, nums, target):
    #     """
    #     将问题视作背包变体
    #     现有 物品 nums，要装买体积为 target 的背包
    #     如果装入 nums[i]，背包体积减少 nums[i], 如果不装，背包提及反而增加 nums[i]
    #     问有多少种装法
    #     """
    #     # memo[idx] 表示 到 nums[idx] 的数列，达到某个 target，有多少种方法
    #     memo = [{} for _ in range(len(nums))]
    #     # 初始化，只有第一个数时，想达成的 target == nums[0] 时，有一种方法
    #     memo[0][nums[0]] = 1
    #     memo[0][-nums[0]] = 1
    #     print(memo)
    #     for idx in range(1, len(nums)):
    #         for tgt in range(target + 1):
    #             print(memo, idx, tgt)
    #             # 如果 memo[idx - 1] 中，不含 tgt - nums[idx] 说明 加法无法达成
    #             if not (tgt - nums[idx]) in memo[idx - 1].keys():
    #                 add_current = 0
    #             else:
    #                 add_current = memo[idx - 1][tgt - nums[idx]]
    #             # 减法分支同理
    #             if not (tgt - nums[idx]) in memo[idx - 1].keys():
    #                 sub_cuurent = 0
    #             else:
    #                 sub_cuurent = memo[idx - 1][tgt + nums[idx]]
    #             if add_current + sub_cuurent:
    #                 memo[idx][tgt] = add_current + sub_cuurent
    #     print(memo)
        

    def test(self):
        nums = [1, 1, 1, 1, 1]
        target = 3
        ans = self.target_sum_dp_backpack(nums, target)
        print(ans)


soln = Solution()
soln.test()