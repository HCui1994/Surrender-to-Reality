"""
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. 
If there is more than one possible answer, return the longest word with the smallest lexicographical order.
If there is no answer, return the empty string.

Example 1:
Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:
Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

Note:
1.  All the strings in the input will only contain lowercase letters.
2.  The length of words will be in the range [1, 1000].
3.  The length of words[i] will be in the range [1, 30].
"""

class Solution:

    def __init__(self):
        self._max_length = 0


    def longest_word(self, words):
        trie = self._build_trie(words)
        words = set(words)
        # print(words)
        res = {}
        self._traverse(trie, "", words, 0, res)
        return min(res[self._max_length])


    def _traverse(self, trie, prefix, words, depth, res):            
        for char in trie:
            if char == "final" and depth >= self._max_length:
                self._max_length = depth
                res.setdefault(self._max_length, set([trie["final"]]))
                res[self._max_length].add(prefix)
            elif (prefix + char) in words:
                # print(prefix + char)
                self._traverse(trie[char], prefix + char, words, depth + 1, res)
        


    def _build_trie(self, words):
        trie = {}
        for word in words:
            focus = trie
            for char in word:
                focus = focus.setdefault(char, {})
            focus["final"] = word
        return trie


    def test(self):
        words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
        print(self.longest_word(words))


Solution().test()