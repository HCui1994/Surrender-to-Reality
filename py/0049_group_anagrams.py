"""
Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

SCORE:
1950 -> 2004 -> 2010 
    TLE     ac
40.03
"""
import collections
class Solution(object):
    def group_anagrams(self, strs):
        """
        TLE
        """
        anagrams_dict = {}
        for i, string in enumerate(strs):
            letters = tuple(sorted(string))
            # print(letters)
            if letters not in anagrams_dict.keys():
                anagrams_dict[letters] = [string]
            else:
                anagrams_dict[letters].append(string)
        # print(anagrams_dict)
        # res = []
        # for _, item in anagrams_dict.items():
        #     temp = []
        #     for idx in item:
        #         temp.append(strs[idx])
        #     res.append(temp)
        return list(anagrams_dict.values())

    def group_anagrams_2(self):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

    def test(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        print(self.group_anagrams(strs))


Solution().test()