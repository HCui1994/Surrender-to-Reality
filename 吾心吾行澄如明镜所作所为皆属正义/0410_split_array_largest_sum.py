"""
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. 
Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""

class Solution(object):
    def split_array(self, nums, m):
        self.cum_sum_array = []
        cum_sum = 0
        for num in nums:
            cum_sum += num
            self.cum_sum_array.append(cum_sum)
        self.memo = {}
        

    def splitter(self, end, m):
        if m == 1:
            return self.cum_sum_array[end]
        if (end, m) in self.memo:
            return self.memo[end, m]
        