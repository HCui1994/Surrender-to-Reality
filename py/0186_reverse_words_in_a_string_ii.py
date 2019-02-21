"""
Given an input string , reverse the string word by word. 

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

Note: 
A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?
"""

class Solution:

    def reverse_words(self, str):
        idx = 0
        while idx < len(str):
            start = idx
            while idx < len(str) and str[idx] != " ":
                idx += 1
            end = idx
            word = str[start : end]
            self._swapper(str, start, end)
            idx += 1
        str_len = len(str)
        self._reverser(str, 0, len(str))
    
        # str = str[::-1]

    def _reverser(self, str, start, end):
        for idx in range((end - start) // 2):
            str[start + idx], str[end - 1 - idx] = str[end - 1 - idx], str[start + idx]

    def test(self):
        str = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
        self.reverse_words(str)
        print(str)


soln = Solution()
soln.test()
    
        