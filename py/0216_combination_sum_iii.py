"""
Find all possible combinations of k numbers that add up to a number n
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""
from itertools import combinations

class Solution(object):
    def combination_sum_stdlib(self, k, n):
        return [comb for comb in combinations(range(1, 10), k) if sum(comb) == n]