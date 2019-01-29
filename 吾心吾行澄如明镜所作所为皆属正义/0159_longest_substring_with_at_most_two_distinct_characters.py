"""
Given a string s, find the length of the longest substring t, that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
"""

import collections

class Solution(object):
    def len_of_longest_substring(self, s):
        basket = collections.Counter()
        ndiff = 0
        max_length = 0
        left = 0
        for right, right_letter in enumerate(s):
            if right_letter not in basket:
                ndiff += 1
            basket[right_letter] += 1
            while ndiff > 2:
                left_letter = s[left]
                basket[left_letter] -= 1
                if basket[left_letter] == 0:
                    del basket[left_letter]
                ndiff -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        print(max_length)

    def test(self):
        s = "eceba"
        self.len_of_longest_substring(s)
    

Solution().test()
                
