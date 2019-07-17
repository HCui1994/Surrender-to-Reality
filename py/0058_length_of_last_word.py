"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.

Example:
Input: "Hello World"
Output: 5
"""

class Solution(object):
    def length_of_last_word(self, s: str) -> int:
        s = s.split(' ')
        for e in s[::-1]:
            if e != "":
                return len(e)
        return 0