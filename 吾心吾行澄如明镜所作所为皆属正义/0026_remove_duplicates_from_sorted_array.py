"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length.

Clarification:
Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.
Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""


class Solution(object):
    def remove_duplicates(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        skip = 1  # 初始化，设定跳过了一个数字
        idx = 1  # 初始化，从数列下标 1 开始遍历
        count = 1  # 统计有多少个不同的数字
        while idx < len(nums):
            if nums[idx] == nums[idx - skip]:
                # 如果当前数字与最有一个有效数字相等，当前数字视为无效，即 skip 值自增
                skip += 1
            else:
                # 如果当前数字与最后一个有效数字不等，当前数字视为有效，并至于最后一个有效数字之后，skip 值不自增，count 自增
                nums[idx - skip + 1] = nums[idx]
                count += 1
            idx += 1
        # print(nums, count)
        return count  # count == idx - skip + 1

    def test(self):
        nums = [0]
        self.remove_duplicates(nums)


Solution().test()
