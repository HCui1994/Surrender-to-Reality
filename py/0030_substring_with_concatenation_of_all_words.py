"""
You are given a string, s, and a list of words, words, that are all of the same length.
Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:
Input:
s = "barfoothefoobarman",
words = ["foo","bar"]

Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:
Input:
s = "wordgoodgoodgoodbestword",
words = ["word","good","best","word"]
Output: []
"""

import collections


class Solution(object):

    def find_substring(self, string, words):
        """
        brutal
        """
        if not words or not string:
            return []
        num_words = len(words)
        word_len = len(words[0])
        res = []
        # print(len(string) - word_len *num_words)
        for i in range(len(string) - word_len * num_words + 1):
            words_counter = collections.Counter(words)
            start = i
            # print(i)
            while start < len(string) - word_len + 1 and words_counter:
                word = string[start: start + word_len]
                if word in words_counter:
                    # print(word)
                    words_counter[word] -= 1
                    if words_counter[word] == 0:
                        del words_counter[word]
                else:
                    break
                start += word_len
            if not words_counter:
                res.append(i)
        # print(res)
        return res

        

    def test(self):
        string = "wordgoodgoodgoodbestword"
        words = ["word", "good", "best", "good"]

        string = "barfoothefoobarman"
        words = ["foo", "bar"]
        self.find_substring(string, words)


print(Solution().test())
