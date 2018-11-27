"""
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:
Input:
s = "aaabb", k = 3
Output:
3
The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:
Input:
s = "ababbc", k = 2
Output:
5
The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""

class Solution:
    def longest_sub_string(self, s, k):
        """
        直觉告诉我这是一个 dp 问题，考虑子问题是什么？（并不是）
        在暴力求解的基础上改为分治求解
        """
        # print(s, k)
        if len(s) < k:
            return 0
        letter_dict = {}
        for idx, letter in enumerate(s):
            if not letter in letter_dict.keys():
                letter_dict[letter] = [idx]
            else:
                letter_dict[letter].append(idx)
        split = [-1, len(s)]
        # print(split)
        for key, value in letter_dict.items():
            if len(value) < k:
                # print(value)
                split += value
        split = sorted(split)
        if len(split) == 2:
            return split[-1]
        max_length = 0
        for idx in range(len(split) - 1):
            start = split[idx] + 1
            end = split[idx + 1]
            max_length = max(max_length, self.longest_sub_string(s[start: end], k))
        return max_length

    
    def test(self):
        s = "qqwweerrttyyuuiiop"
        k = 2
        print(self.longest_sub_string(s, k))


Solution().test()
