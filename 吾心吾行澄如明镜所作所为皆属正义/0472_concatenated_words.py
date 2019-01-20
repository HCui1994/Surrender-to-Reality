"""
Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

Note:
The number of elements of the given array will not exceed 10,000
The length sum of elements in the given array will not exceed 600,000.
All the input string will only include lower case letters.
The returned elements order does not matter.
"""


class Solution(object):
    def concatenated_words_memoization(self, words):
        words = set(words)
        memo = set(words)
        if "" in memo:
            memo.remove("")
            words.remove("")
        res = []
        for word in words:
            memo.remove(word)
            if self.memoization_helper(word, memo):
                res.append(word)
            memo.add(word)
        print(memo)
        return res

    def memoization_helper(self, string, memo):
        # print(string)
        if not string or string in memo:
            return True
        for word in memo:
            word_length = len(word)
            if string[:word_length] == word and self.memoization_helper(string[word_length:], memo):
                memo.add(string)
                return True
        return False

    def concatenated_words_recursion(self, words):
        self.words_set = set(words)
        res = []
        for word in words:
            if self.recursion_helper(word):
                res.append(word)
        return res

    def recursion_helper(self, string):
        for breaking_point in range(1, len(string)):
            if string[:breaking_point] in self.words_set:
                if string[breaking_point:] in self.words_set:
                    return True
                elif self.recursion_helper(string[breaking_point:]):
                    return True
        return False

    def concatenated_words_dp(self, words):
        def key(element):
            return len(element)
        words = sorted(words, key=key)
        unavailable_set = set()
        res_set = set()
        for concatenation in words:
            dp = [False for _ in range(len(concatenation) + 1)]
            dp[0] = True
            temp_set = set()
            for i in range(len(concatenation)):
                dpi = i + 1
                for word in words:
                    word_len = len(word)
                    if i + 1 >= word_len and word == concatenation[i + 1 - word_len: i + 1]:
                        dp[dpi] = dp[dpi] or dp[dpi - word_len]
                        if dp[dpi]:
                            temp_set.add(concatenation[:i+1])
            temp_set.remove(concatenation)
            unavailable_set = unavailable_set | temp_set
            if sum(dp[1:-1]):
                res_set.add(concatenation)
        # print(res_set)
        # print(unavailable_set)   
        # print(res_set - unavailable_set)
        return res_set - unavailable_set

    def word_break_1_dp(self, string, words):
        def key(element):
            return len(element)
        words = sorted(words, key=key)
        dp = [False for _ in range(len(string) + 1)]
        dp[0] = True
        for i in range(len(string)):
            dpi = i + 1
            for word in words:
                word_len = len(word)
                print(string[i - word_len + 1: i + 1])
                if i + 1 >= word_len and word == string[i - word_len + 1: i + 1]:
                    dp[dpi] = dp[dpi] or dp[dpi - word_len]
        print(dp)
        return dp[-1]

    def test(self):
        words = ["cat", "cats", "catsdogcats", "dog",
                 "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
        print(self.concatenated_words_dp(words))
        # print(self.word_break_1_dp(string="dogcatsdogratcatdogcatdogcatsdoghippopotamuses", words=words))


Solution().test()