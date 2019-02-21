"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. 
Assume that there is only one duplicate number, find the duplicate one.

Example 1:
Input: [1,3,4,2,2]
Output: 2

Example 2:
Input: [3,1,3,4,2]
Output: 3

Note:
1.  You must not modify the array (assume the array is read only).
2.  You must use only constant, O(1) extra space.
3.  Your runtime complexity should be less than O(n^2).
4.  There is only one duplicate number in the array, but it could be repeated more than once.
"""


class Solution(object):
    def find_duplicate_binary_search(self, nums):
        """
        不能 hash，不能 sort，不能 brute force
        尝试二分求解 O(nlogn)
        http://www.cnblogs.com/grandyang/p/4843654.html
        虽然不能对给定的 nums 数列进行排序，但由于 num in [1, n] 的特性，可以抽象一个排好序的数列，用二分法寻找
        假设 mid 为寻找的数字，遍历数列，数有多少个数小于等于 mid。
        如果 target <= mid，即从 1 到 mid 有 mid + 1 个数，进而可以缩小范围
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count <= mid:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def find_duplicate_two_pointers(self, nums):
        """
        鸽巢定理证明，O(n)
        http://bookshadow.com/weblog/2015/09/28/leetcode-find-duplicate-number/
        """
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        print(slow, fast)
        finder = 0
        while True:
            slow = nums[slow]
            finder = nums[finder]
            if slow == finder:
                break
        return finder

    def find_duplicate_number_bit_manipulate(self, nums):
        pass

    def test(self):
        nums = [1, 1]
        print(self.find_duplicate_binary_search(nums))


Solution().test()
