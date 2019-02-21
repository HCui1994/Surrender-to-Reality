"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
    add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Example 2:
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""

import time

class Solution(object):
    def word_break_dp(self, string, word_dict):
        """
        MLE
        """
        dp = [[] for _ in range(len(string))]
        # init
        for word in word_dict:
            if word == string[:len(word)]:
                dp[len(word) - 1].append([word + " "])
        print(dp)
        for idx in range(len(string)):
            for word in word_dict:
                word_length = len(word)
                if word_length < idx + 1 and word == string[idx - word_length + 1: idx + 1] and dp[idx - word_length]:
                    print(word, dp[idx - word_length])
                    time.sleep(1)
                    for prev_words in dp[idx - word_length]:
                        dp[idx].append(prev_words + [word + " "])
        print(dp[-1])
        res = ["".join(words)[:-1] for words in dp[-1]]
        print(res)
        return res

    def word_break_brutal(self, string, word_dict):
        res = []
        self.brutal_helper(string, word_dict, "", res)
        print(res)
        return res

    def brutal_helper(self, string, word_dict, prev_res, res):
        print(string, prev_res)
        if not string:
            res.append(prev_res[:-1])
        for word in word_dict:
            if string[: len(word)] == word:
                self.brutal_helper(string[len(word):], word_dict, prev_res + word + " ", res)

    def word_break_memoization(self, string, word_dict):
        """
        与 brutal 方法类似的是，采用了递归方法
        但与 brutal 方法不同的是，从 string 的末尾开始记录
        TLE ?? 
        """
        memo = {}
        return self.memoization_helper(string, word_dict, memo)

    def memoization_helper(self, string, word_dict, memo):
        if memo.get(string):
            return memo[string]
        if not string:
            return [""]
        res = []
        for word in word_dict:
            word_length = len(word)
            if string[:word_length] != word:
                continue
            # print(word, string, word_length)
            valid_list = self.memoization_helper(string[word_length:], word_dict, memo)
            for valid_seq in valid_list:
                res.append(word + (" " if valid_seq else "") + valid_seq)
        memo[string] = res
        return memo[string]

    def test(self):
        s = "aaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaa"
        wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
        print(self.word_break_memoization(s, wordDict))


Solution().test()
