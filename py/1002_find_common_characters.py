"""
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  
For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

Example 1:
Input: ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: ["cool","lock","cook"]
Output: ["c","o"]
"""

import collections

class Solution(object):
    def common_chars(self, words):
        if not words:
            return []
        cnt = collections.Counter(words[0])
        for word in words[1:]:
            temp_cnt = collections.Counter(word)
            intersection = temp_cnt.keys() & cnt.keys()
            new_cnt = collections.Counter()
            for key in intersection:
                new_cnt[key] = min(cnt[key], temp_cnt[key])
            cnt = new_cnt
        res = []
        for key, val in cnt.items():
            for _ in range(val):
                res.append(key)
        return res