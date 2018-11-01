class Solution:
    def moveZeors(self, nums):
        if not nums:
            return
        elif len(nums) <= 2 and nums[0] == 0:
            nums[0], nums[len(nums) - 1] = nums[len(nums) - 1], nums[0]

        # 每个pass总能将最大的元素“浮上”数组末尾
        # 下个pass可以少考虑1个元素
        for passnum in range(len(nums)-1, 0, -1):
            for i in range(passnum):
                if nums[i] == 0:
                    nums[i], nums[i+1] = nums[i+1], nums[i]

soln = Solution()
nums = [0, 1,3,4,2,5,0,0,1,1,3,0,1]
soln.moveZeors(nums)
print(nums)