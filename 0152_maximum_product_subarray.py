"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
import numpy as np
class Solution:
    def maxProduct(self, nums):
        """Brutal TLE"""
        if not nums:
            return 0
        length = len(nums)
        memo = [[None for _ in range(length)] for _ in range(length)]
        for i in range(length):
            memo[i][i] = nums[i]
        max_product = -float("inf")
        for i in range(length):
            for j in range(i, length, +1):
                if i == j:
                    memo[i][j] = nums[i]
                else:
                    memo[i][j] = memo[i][j - 1] * memo[j][j]
                max_product = max(memo[i][j], max_product)
        return max_product

    def max_product_one_pass(self, nums):
        """one pass"""
        if not nums:
            return 0
        length = len(nums)
        # local_max, local_min：到当前元素为终点的子数列的 极大值，极小值
        local_max = local_min = 1
        global_max = nums[0]
        print(nums)
        print("num: {}\tloc_max: {}\tloc_min: {}\tglb_max: {}".format("init", local_max, local_min, global_max))
        for num in nums:
            if num < 0:
                # 如果当前元素小于0，极大值和极小值在乘以当前元素后，会发生互换
                # 如果原local_min为负，乘以负值之后变正值，成为了local_max，但是不一定比原来的local_max大
                # 如果原local_min为正，成以负值以后变负值，成为新local_min
                # 如果原local_min为正 （loc_max其实一直为正），原loc_max必然为正，且比原loc_min大，则原loc_max乘以负值以后成为更小的负数，成为loc_min
                # 但是要保证local_max为正
                local_min, local_max = local_max * num, max(local_min * num, 1)
                global_max = max(global_max, local_max)
            elif num > 0:
                # 如果当前元素大于0,极大值和极小值的绝对值都会被放大
                # local_max只可能为正，乘以正值成为更大的local_max
                local_max *= num
                local_min *= num
                global_max = max(global_max, local_max)
            else:
                # 如果当前元素等于0，子数组重置
                local_max = local_min = 1
                global_max = max(global_max, 0)
            print("num: {}\tloc_max: {}\tloc_min: {}\tglb_max: {}".format(num, local_max, local_min, global_max))
        return global_max

    def max_prodcut_naive_dp(self, nums):
        """
        有时候做题目应该有一种大局观，从细节中解脱出来。
        这点类似于做物理题时，不一定非要用动力学原理弄清整个过程和每个细节，有时候用简单的从功和能的角度，只关注最终状态也可以顺利解题。
        
        需要维护的当前最大值和当前最小值，都是在dp_min[i-1] * A[i]，dp_max[i] * A[i]，和A[i]这三者里面取一即可。
        有了这个只关乎最终状态，不关乎过程细节的结论，解题过程可以大大简化。
        """
        length = len(nums)
        memo_local_max = [None for _ in nums]
        memo_local_min = [None for _ in nums]
        memo_local_max[0] = memo_local_min[0] = nums[0]
        for idx in range(1, length, +1):
            # 比较前一极大值乘以当前数，前一极小值乘以当前数，当前数
            # 如果三者中：
            # 前一极大值乘以当前数最大，毫无疑问，更新当前极大值
            # 前一极小值乘以当前数最大，毫无疑问，更新当前极大值
            # 当前数最大，重置子数组，当前极大值即为当前数
            memo_local_max[idx] = max([memo_local_max[idx - 1] * nums[idx], memo_local_min[idx - 1] * nums[idx], nums[idx]])
            memo_local_min[idx] = min([memo_local_max[idx - 1] * nums[idx], memo_local_min[idx - 1] * nums[idx], nums[idx]])
        print(memo_local_max)
        print(memo_local_min)

    def max_product_mem_opt_dp(self, nums):
        """ 这个方法真是好理解， 为什么自己想不到 """
        length = len(nums)
        local_max = local_min = nums[0]
        global_max = local_max
        for num in nums[1:]:
            temp_local_max = max([local_max * num, local_min * num, num])
            temp_local_min = min([local_max * num, local_min * num, num])
            local_max, local_min = temp_local_max, temp_local_min
            global_max = max(global_max, local_max)
        return global_max



soln = Solution()
nums = [2,3,-2,4]
ans = soln.max_product_mem_opt_dp(nums)
print(ans)