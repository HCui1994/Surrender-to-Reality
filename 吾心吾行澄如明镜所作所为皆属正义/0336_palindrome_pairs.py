
class Solution:
    def palindromePairs(self, words):
        """
        创建 trie 树，之后遍历 word，对 word 逆序 并在 trie 树中查找前缀
        四种情况：
        1. 某个 word 的逆序不是 trie 树某个分支的前缀，return
        2. 某个 word 的逆序是 trie 的某个完整的分支，若该 word 与 trie 分支不是同一个 instance，添加到结果集
        3. 某个 word 的逆序是 trie 某个分支的前缀，若 trie 该分支剩余的序列是回文序列，添加到结果集
        4. trie 的某个分支是 word 逆序的前缀，若 word 剩余序列是回文序列，添加到结果集
        """
        trie = self._build_trie(words)
        res = set()
        num_words = len(words)
        for i, word in enumerate(words):
            if word == "":
                for j, another_word in enumerate(words):
                    if i == j:
                        continue
                    elif self._is_palindrome(another_word):
                        res.add((i, j))
                        res.add((j, i))
            self._search(trie, word[::-1], i, res)
        return list(res)

    def _build_trie(self, words):
        trie = {}
        for idx, word in enumerate(words):
            focus = trie
            for char in word:
                focus = focus.setdefault(char, {})
            focus.setdefault("index", idx)
        return trie
    
    def _search(self, trie, word, idx, res):
        for i, char in enumerate(word):
            if trie.get("index") is not None and self._is_palindrome(word[i:]):
                # print("case 4")
                # case 4: trie 的某个完整分支是 word 逆序的前缀
                res.add((trie["index"], idx))
                return
            if char not in trie.keys():
                # case 1: 某个 word 的逆序不是 trie 树某个分支的前缀
                # print("case 1")
                return
            trie = trie[char]
        if trie.get("index") is not None and idx != trie["index"]:
            # print("case 2")
            # case 2: 某个 word 的逆序是 trie 的某个完整分支，且该逆序与分支不是同一 instance
            res.add((trie["index"], idx))
            res.add((idx, trie["index"]))
            return
        else:
            # print("case 3")
            # case 3: 某个 word 的逆序是 trie 某个分支的前缀
            self._dfs_trie(trie, idx, "", res)
            

    def _is_palindrome(self, word):
        if not word:
            return False
        length = len(word)
        stack = list(word[:length // 2])
        if length % 2:
            idx = length // 2 + 1
        else:
            idx = length // 2
        while idx < length:
            if word[idx] == stack[-1]:
                stack.pop()
            else:
                return False
            idx += 1
        return True

    def _dfs_trie(self, trie, idx, word_remain, res):
        if trie.get("index") is not None and self._is_palindrome(word_remain):
            res.add((idx, trie["index"]))
            print(word_remain, res)
            return
        for char in trie.keys():
            if char == "index":
                continue
            self._dfs_trie(trie[char], idx, word_remain + char, res)
    
    def test(self):
        words = ["", "", ""]
        trie = self._build_trie(words)
        print(trie)


Solution().test()
