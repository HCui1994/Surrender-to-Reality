"""
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a^2 + b^2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
Input: 3
Output: False
"""
import math
class Solution:
    def judge_square_sum(self, c):
        square_set = set([])
        for i in range(int(math.sqrt(c)) + 1):
            square_set.add(i ** 2)
        print(square_set)
        for a in square_set:
            if (c - a) in square_set:
                return True
        return False
    
    def test(self):
        c = 5
        print(self.judge_square_sum(c))
    

soln = Solution()
soln.test()
        