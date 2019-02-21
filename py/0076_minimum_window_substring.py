"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""

import collections


class Solution(object):
    def min_window(self, s, t):
        if not t or not s:
            return ""
        t_counter = collections.Counter(t)
        s_counter = collections.Counter()
        left = right = 0
        in_position = 0
        min_window_size = float("inf")
        res = ""
        while right < len(s):
            if s[right] in t_counter:
                s_counter[s[right]] += 1
                if s_counter[s[right]] == t_counter[s[right]]:
                    in_position += 1
            while left <= right and in_position == len(t_counter):
                print(s[left:right+1], min_window_size)
                if s[left] in t_counter:
                    s_counter[s[left]] -= 1
                    if s_counter[s[left]] < t_counter[s[left]]:
                        in_position -= 1
                        if right - left + 1 < min_window_size:
                            min_window_size = right - left + 1
                            res = s[left: right + 1]
                left += 1
            right += 1
        return res

    def check(self, s_counter, t_counter):
        for key, value in t_counter.items():
            if s_counter[key] != value:
                return False
        return True

    def test(self):
        s = "cabwefgewcwaefgcf"
        t = "cae"
        print(self.min_window(s, t))


Solution().test()
