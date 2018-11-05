class Solution:
    def maxSubArray(self, nums):
        """
        Args:
            nums: [num1, num2, ...] of Integer
        Returns:
            max_sub_array summation of Integer  
        """
        memo = [None for _ in nums]
        memo[0] = nums[0]
        # print("num\tmemo\tnum+memo")
        for idx in range(1, len(nums), +1):
            # 最大子序列必须是连续的，也就是每个数字都要选择
            # 不存在 选 与 不选 的判断
            # 需要判断的事，从哪里开始连续
            # print("{}\t{}\t{}".format(nums[idx], memo[idx-1], nums[idx] + memo[idx - 1]))
            if nums[idx] > nums[idx] + memo[idx - 1]:
                memo[idx] = nums[idx]
            else:
                memo[idx] = memo[idx - 1] + nums[idx]
        return max(memo)

    def max_subarray_mem_opt(self, nums):
        memo = nums[0] 
        max_subarray = memo
        for idx in range(1, len(nums), +1):
            if nums[idx] > nums[idx] + memo:
                memo = nums[idx]
            else:
                memo += nums[idx]
            if memo > max_subarray:
                max_subarray = memo
        return max_subarray


soln = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(soln.max_subarray_mem_opt(nums))
