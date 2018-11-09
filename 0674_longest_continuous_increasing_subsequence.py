class Solution:
    def findLengthOfLCIS(self, nums):
        max_length = 0
        if not nums:
            return max_length
        length = 1
        max_length = length
        for idx in range(1, len(nums), +1):
            if nums[idx] > nums[idx - 1]:
                length += 1
                if length > max_length:
                    max_length = length
            else:
                length = 1
        return max_length


soln = Solution()
nums = [2,2,2,2,2]
ans = soln.findLengthOfLCIS(nums)
print(ans)