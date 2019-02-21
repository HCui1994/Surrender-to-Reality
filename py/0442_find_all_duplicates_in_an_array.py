"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""

class Solution(object):
    def find_duplicates(self, nums):
        """
        关键的两点：
        1.  1 ≤ a[i] ≤ n (n = size of array)，所有的数字都小于等于数组长度
        2.  some elements appear twice and others appear once 每个数字最多出现两次
        所以可以用 num 自身作为数组下标进行访问
        """
        ans = []
        for num in nums:
            temp = abs(num)
            if nums[temp - 1] > 0:
                nums[temp - 1] *= -1
            else:
                ans.append(temp)
        return ans
    
    def test(self):
        nums = [4,3,2,7,8,2,3,1]
        print(self.find_duplicates(nums))


soln = Solution()
soln.test()