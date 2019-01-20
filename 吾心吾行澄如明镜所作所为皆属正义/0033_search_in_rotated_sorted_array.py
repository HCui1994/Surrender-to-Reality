"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""


class Solution(object):
    def seatch_in_rotated_array(self, nums, target):
        """
        二分查找。关键在于确定下一个寻找的区间在左侧还是在右侧
        考虑数列 [ 5 6 7 8 9    |    0 1 2 3 4 ]
        分为        左段                 右段
        或      [ 0 1 2 3 4    |    5 6 7 8 9 ]
        left 为左段第一个数，right 为右段最后一个数
        
        case1：mid > left，mid 在左段中
            case1.1：target < mid, target > left，target 在 mid 左侧
            case1.2：否则，target 在 mid 右侧
        case2：mid < right，mid 在右段中
            case2.1：target > mid, target < right，target 在 mid 右侧
            case2.2：否则，target 在 mid 左侧
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            elif nums[mid] == target:
                return mid
            
            if nums[left] < nums[mid]: # mid 在左段
                if nums[left] < target and target < nums[mid]: # target 在 mid 左侧
                    right = mid - 1
                else:   # 否则，target 在 mid 右侧
                    left = mid + 1
            else:
                if nums[mid] < target and target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    def test(self):
        nums = [1]
        target = 1
        print(self.seatch_in_rotated_array(nums, target))


Solution().test()
