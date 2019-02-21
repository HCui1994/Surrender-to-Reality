"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:
1.  Return 0 if there is no such transformation sequence.
2.  All words have the same length.
3.  All words contain only lowercase alphabetic characters.
4.  You may assume no duplicates in the word list.
5.  You may assume beginWord and endWord are non-empty and are not the same.

Example 1:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""


class Solution:
    def ladder_length(self, begin_word, end_word, word_list):
        """
        bfs
        建立 word_list 集合，建立 word_visited 字典
        每个单词第一次访问到的距离，就是从 begin_word 到达该单词的最短距离
        之后再访问到该单词，跳过，不做任何事

        投入湖面的石子泛起的涟漪一圈圈扩散，直到碰到湖中立起的一支荷花
        """
        letter_bank = {idx: set() for idx in range(len(begin_word))}
        for word in word_list:
            for idx in range(len(begin_word)):
                letter_bank[idx].add(word[idx])
        # print(letter_bank)
        word_list = set(word_list)
        word_visited = {begin_word: 1}
        queue = [begin_word]
        while queue:
            print(word_visited)
            current_word = queue.pop(0)
            for idx in range(len(begin_word)):
                current_word_to_list = list(current_word)
                for letter in letter_bank[idx]:
                    current_word_to_list[idx] = letter
                    next_word = "".join(current_word_to_list)
                    if next_word in word_list and next_word == end_word:
                        return word_visited[current_word] + 1
                    elif next_word in word_list and next_word not in word_visited.keys():
                        word_visited[next_word] = word_visited[current_word] + 1
                        queue.append(next_word)
        return 0

    def ladder_length_double_bfs(self, begin_word, end_word, word_list):
        word_list = set(word_list)
        if end_word not in word_list:
            return 0
        # preprocess
        letter_bank = {idx: set() for idx in range(len(begin_word))}
        for word in word_list:
            for idx in range(len(begin_word)):
                letter_bank[idx].add(word[idx])

        begin_set, end_set = set([begin_word]), set([end_word])
        visited = set([begin_word, end_word])
        path_len, word_len = 2, len(begin_word)
        while begin_set and end_set:
            
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
            print(begin_set, end_set)
            temp_set = set()
            for word in begin_set:
                word_to_list = list(word)
                for idx in range(word_len):
                    letter_backup = word_to_list[idx]
                    for letter in letter_bank[idx]:
                        word_to_list[idx] = letter
                        next_word = "".join(word_to_list)
                        if next_word in end_set:
                            return path_len
                        if next_word in word_list and next_word not in visited:
                            temp_set.add(next_word)
                            # visited.add(next_word)
                    word_to_list[idx] = letter_backup
            visited = visited.union(temp_set)
            begin_set = temp_set
            path_len += 1
        return 0
                        

    def test(self):
        # beginWord = "hit"
        # endWord = "cog"
        # wordList = ["hot","dot","dog","lot","log"]
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        print(self.ladder_length_double_bfs(beginWord, endWord, wordList))


Solution().test()
