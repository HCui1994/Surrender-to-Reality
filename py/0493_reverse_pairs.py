"""
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:
Input: [1,3,2,3,1]
Output: 2

Example2:
Input: [2,4,3,5,1]
Output: 3

Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.
"""

class Solution(object):
    def reverse_pairs_brutal(self, nums):
        """
        TLE（必然。。。）
        """
        n = len(nums)
        count  = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] > 2 * nums[j]:
                    count += 1
        print(count)
        return count

    def reverse_pairs_binary_search()

    def test(self):
        self.reverse_pairs_brutal([1,3,2,3,1])


Solution().test()