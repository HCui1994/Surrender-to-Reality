"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
word1 and word2 may be the same and they represent two individual words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Input: word1 = “makes”, word2 = “coding”
Output: 1
Input: word1 = "makes", word2 = "makes"
Output: 3

Note:
You may assume word1 and word2 are both in the list.
"""

class Solution:
    def shortest_word_distance(self, words, word1, word2):
        """
        hash map (dict)
        """
        index_dict = {}
        for idx, word in enumerate(words):
            if not word in index_dict.keys():
                index_dict[word] = [idx]
            else:
                index_dict[word].append(idx)
        idx_list_1 = index_dict[word1]
        idx_list_2 = index_dict[word2]
        min_dist = float("inf")
        if word1 != word2:
            for idx1 in idx_list_1:
                for idx2 in idx_list_2:
                    min_dist = min(min_dist, abs(idx1 - idx2))
        else:
            for idx in range(len(idx_list_1) - 1):
                min_dist = min(min_dist, idx_list_1[idx + 1] - idx_list_1[idx])
        return min_dist


    def test(self):
        words = ["practice", "makes", "perfect", "coding", "makes"]
        word1 = "makes"
        word2 = "makes"
        self.shortest_word_distance(words, word1, word2)
    
Solution().test()