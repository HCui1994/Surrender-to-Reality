"""
Given an input string, reverse the string word by word.
Example:  
Input: "the sky is blue",
Output: "blue is sky the".
Note:
A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
Follow up: For C programmers, try to solve it in-place in O(1) space.
"""

class Solution(object):
    def reverse_words(self, string):
        word_list = string.split(' ')
        word_list = [word[::-1] for word in word_list]
        res = ""
        for word in word_list:
            if word:
                res += word + " "
        return res[:-1][::-1]
    
    def test(self):
        print(self.reverse_words("the sky  is blue   shit "))


Solution().test()