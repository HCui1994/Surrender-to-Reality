"""
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, 
i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]
"""

import collections


class Solution:
    def palindromePairs(self, words):

        def check_palindrome(word):
            for i in range(len(word) // 2):
                if word[i] != word[len(word) - i - 1]:
                    return False
            return True

        original_set = {key: value for value, key in enumerate(words)}
        reversed_set = {key[::-1]: value for value, key in enumerate(words)}
        res = set()
        for word, i in original_set.items():
            for index in range(1, len(word) + 1):
                if word[:index] in reversed_set and i != reversed_set[word[:index]] and check_palindrome(word[index:]):
                    res.add((i, reversed_set[word[:index]]))
        for word, i in reversed_set.items():
            for index in range(1, len(word) + 1):
                if word[:index] in original_set and i != original_set[word[:index]] and check_palindrome(word[index:]):
                    res.add((i, original_set[word[:index]]))
        return list(res)


if __name__ == "__main__":
    soln = Solution()
    soln.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])
