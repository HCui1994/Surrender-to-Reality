"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:
1.  Return an empty list if there is no such transformation sequence.
2.  All words have the same length.
3.  All words contain only lowercase alphabetic characters.
4.  You may assume no duplicates in the word list.
5.  You may assume beginWord and endWord are non-empty and are not the same.

Example 1:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

Example 2:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
import collections


class Solution(object):
    def find_ladders_dfs(self, begin_word, end_word, word_list):
        """
        TLE
        """
        self.res = []
        self.end_word = begin_word, end_word
        self.graph = self.build_graph(begin_word, word_list)
        print(self.graph)
        self.path = {word: {"len": float("inf"), "path": []}
                     for word in word_list}
        visited = set()
        self.tracer(begin_word, [begin_word], 1, visited)
        # print(self.path[end_word])
        return self.path[end_word]["path"]

    def tracer(self, node, path, length, visited):
        print(path, node)
        if node in visited:
            return
        visited.add(node)
        if node in self.path:
            if length < self.path[node]["len"]:
                self.path[node]["path"] = [path]
                self.path[node]["len"] = length
            elif length == self.path[node]["len"]:
                self.path[node]["path"].append(path)
            else:
                visited.remove(node)
                return
        for succ in self.graph[node]:
            self.tracer(succ, path + [succ], length + 1, visited)
        visited.remove(node)

    def build_graph(self, begin_word, word_list):
        graph = collections.defaultdict(set)
        for word in word_list:
            if self.is_ladder(begin_word, word):
                graph[begin_word].add(word)
        for idx1 in range(len(word_list) - 1):
            for idx2 in range(idx1 + 1, len(word_list)):
                # print(word_list[idx1], word_list[idx2])
                if self.is_ladder(word_list[idx1], word_list[idx2]):
                    graph[word_list[idx1]].add(word_list[idx2])
                    graph[word_list[idx2]].add(word_list[idx1])
        return graph

    def is_ladder(self, word1, word2):
        one_diff = False
        for letter1, letter2 in zip(word1, word2):
            if letter1 != letter2 and not one_diff:
                one_diff += True
            elif letter1 != letter2 and one_diff:
                return False
        return True if one_diff else False

    def find_ladders_tirvial_bfs(self, begin_word, end_word, word_list):
        """
        考虑到bfs的特性，如果发现已经到过一个节点，那么一定绕了远路。
        如何加入重复的路径？
        再次 TLE 。。。

        build graph 的开销太大 O(n^2)，能否优化？
        """
        if end_word not in word_list:
            return []
        graph = self.build_graph(begin_word, word_list)
        queue = [(begin_word, 0, [begin_word])]
        path = {word: {"len": float("inf"), "path": []}
                for word in word_list}
        while queue:
            curr_word, curr_len, curr_path = queue.pop(0)
            for succ_word in graph[curr_word]:
                if curr_len + 1 > path[succ_word]["len"]:
                    continue
                elif curr_len + 1 == path[succ_word]["len"]:
                    path[succ_word]["path"].append(curr_path + [succ_word])
                elif curr_len + 1 < path[succ_word]["len"]:
                    path[succ_word]["len"] = curr_len + 1
                    path[succ_word]["path"] = [curr_path + [succ_word]]
                    queue.append((succ_word, curr_len + 1,
                                  curr_path + [succ_word]))
        print(path[end_word]["path"])

    def find_latters_trivial_bfs_2(self, begin_word, end_word, word_list):
        word_list = set(word_list)
        if end_word not in word_list:
            return []
        letter_bank = self.build_letter_bank(word_list)
        print(letter_bank)
        word_len = len(begin_word)
        path_set = set([(begin_word,)])
        visited = set([begin_word])
        activated = False
        res = []

        while path_set:
            temp_set = set()
            temp_visited = set()
            for path in path_set:
                tail_word_to_list = list(path[-1])
                for idx in range(word_len):
                    letter_backup = tail_word_to_list[idx]
                    for letter in letter_bank[idx]:
                        tail_word_to_list[idx] = letter
                        next_word = "".join(tail_word_to_list)
                        if next_word == end_word:
                            res.append(list(path) + [next_word])
                            activated = True
                        elif next_word in word_list and next_word not in visited:
                            temp_set.add(path + (next_word,))
                            temp_visited.add(next_word)
                    tail_word_to_list[idx] = letter_backup
            if activated:
                break
            visited = visited | temp_visited
            print(visited)
            path_set = temp_set
        print(res)
        return res

    def build_letter_bank(self, word_list):
        letter_bank = collections.defaultdict(set)
        for word in word_list:
            for idx, letter in enumerate(word):
                letter_bank[idx].add(letter)
        return letter_bank

    def find_ladder_double_bfs(self, begin_word, end_word, word_list):
        import collections
        word_list = set(word_list)
        if end_word not in word_list:
            return []

        letter_bank = self.build_letter_bank(word_list)
        word_len = len(begin_word)
        begin_dict = collections.defaultdict(list)
        end_dict = collections.defaultdict(list)
        begin_dict[begin_word] = [[begin_word]]
        end_dict[end_word] = [[end_word]]
        visited = set([begin_word, end_word])
        res = []

        while begin_dict and end_dict and not res:
            # print(visited)
            if len(begin_dict) > len(end_dict):
                begin_dict, end_dict = end_dict, begin_dict
            temp_dict = collections.defaultdict(list)
            for tail_word, begin_paths in begin_dict.items():
                tail_word_to_list = list(tail_word)
                for idx in range(word_len):
                    letter_backup = tail_word_to_list[idx]
                    for letter in letter_bank[idx]:
                        tail_word_to_list[idx] = letter
                        next_word = "".join(tail_word_to_list)
                        # print(next_word, end_dict.keys())
                        if next_word in end_dict:
                            activated = True
                            end_paths = end_dict[next_word]
                            for begin_path in begin_paths:
                                for end_path in end_paths:
                                    res.append(
                                        begin_path + end_path[::-1] if begin_path[0] == begin_word else end_path + begin_path[::-1])
                        elif next_word in word_list and next_word not in visited:
                            for begin_path in begin_paths:
                                temp_dict[next_word].append(
                                    begin_path + [next_word])
                    tail_word_to_list[idx] = letter_backup
            visited = visited | temp_dict.keys()
            begin_dict = temp_dict
        return res

    def test(self):
        print(self.find_ladder_double_bfs("kiss",
                                              "tusk",
                                              ["miss", "dusk", "kiss", "musk", "tusk", "diss", "disk", "sang", "ties", "muss"]))


Solution().test()
