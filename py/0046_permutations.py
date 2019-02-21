"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution(object):
    def permute_recursive(self, nums):
        self.nums = set(nums)
        self.res = []
        self.permute_helper(set(), [])
        return self.res

    def permute_helper(self, used_num, prev_res):
        available_num = self.nums - used_num
        if not available_num:
            self.res.append(prev_res)
        for num in available_num:
            self.permute_helper(used_num | set([num]), prev_res + [num])

    def next_permutation(self, nums):
        """
        如何计算下一个更大的排列
        1. 从后向前扫描，找到第一个不满足递增的数
            如果数字从后向前一直递增，则这一部分是形成了局部最大值
        2. 找到第一个不满足递增的数，该数下标为 i
            需要操作的部分为 num[i:]
        3. 将 num[i] 向后替换。
            从 num[i + 1] 向后扫描，如果 num[i + 1] 大于
        """
        carry_position = len(nums) - 2
        while carry_position >= 0 and nums[carry_position] >= nums[carry_position + 1]:
            # 寻找发生进位的下标
            carry_position -= 1

        if carry_position == -1:
            # 如果进位下标为 -1，说明全数组都从右到左递增
            return nums[::-1]

        switch_position = len(nums) - 1
        while nums[switch_position] <= nums[carry_position]:
            switch_position -= 1
        print(nums[switch_position], nums[carry_position])
        nums[switch_position], nums[carry_position] = nums[carry_position], nums[switch_position]
        nums[carry_position + 1:] = nums[carry_position + 1:][::-1]
        return nums

    def full_permutation(self, nums):
        nums.sort()
        perm = []

        nperm = 1
        for i in range(len(nums)):
            nperm *= (i + 1)
        for _ in range(nperm):
            perm.append([_ for _ in self.next_permutation(nums)])
        return perm

    def test(self):
        nums1 = [1, 2, 3, 4, 5]
        nums2 = [7, 6, 5, 4, 3, 2, 1]
        # print(self.permute_recursive(nums))
        print(self.next_permutation(nums1))


Solution().test()
