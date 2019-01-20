"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
    determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""


class Solution(object):

    def word_break(self, s, wordDict):
        self._string = s
        self._word_set = set(wordDict)
        return self.recursion_breaker(self._string)

    def recursion_breaker(self, string):
        print(string)
        match_flag = False
        if string in self._word_set:
            match_flag = True
        else:
            for word in self._word_set:
                word_length = len(word)
                if word == string[:word_length]:
                    match_flag = match_flag or self.recursion_breaker(
                        string[word_length:])
        return match_flag

    def word_break_dp(self, string, word_dict):
        def key(element):
            return element[1]
        word_dict = sorted([(word, len(word)) for word in word_dict], key=key)
        # print(word_dict)
        dp = [False for _ in range(len(string))]
        # print(dp)
        # 初始化
        for word, length in word_dict:
            if word == string[:length]:
                dp[length - 1] = True
        for i in range(len(string)):
            for word, length in word_dict:
                if i > length - 1 and word == string[i + 1 - length: i + 1]:
                    dp[i] = dp[i] or dp[i - length]
        print(dp)
        return dp[-1]

    def test(self):
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        print(self.word_break_dp(s, wordDict))


Solution().test()
