"""
Given a positive integer N, return the number of positive integers less than or equal to N that have at least 1 repeated digit.

 

Example 1:

Input: 20
Output: 1
Explanation: The only positive number (<= 20) with at least 1 repeated digit is 11.
Example 2:

Input: 100
Output: 10
Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.
Example 3:

Input: 1000
Output: 262
 

Note:

1 <= N <= 10^9
"""
import collections

class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        if N < 11:
            return 0
        # 计算位数
        n = str(n)
        bit_cnt = len(n)
        insert_cnt = bit_cnt - 2
        for insert in range(insert_cnt + 1):
            