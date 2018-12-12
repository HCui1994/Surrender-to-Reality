"""
Given a 2D board and a list of words from the dictionary, find all words in the board.
Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.

Example:

Input: 
words = ["oath","pea","eat","rain"] and 
board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

Output: ["eat","oath"]
Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""


class Solution:
    def find_words(self, board, words):
        if not board or not board[0]:
            return []
        m, n = len(board), len(board[0])
        res = []
        trie = self._build_trie(words)
        for i in range(m):
            for j in range(n):
                self._dfs(board, i, j, m, n, trie, res)
        return res

    def _dfs(self, board, i, j, m, n, trie, res):
        """
        在进入子分支前进行边界检测会导致bug
        假设　 board = ['a']， word = ["a"]
        建立 trie = {'a' : "final" : "a"}}
        由于 board 只有一个格子，向四个方向均无法延伸，算法终止，而无法达到 trie 树的叶节点

        相反，在进入子分支后再进行边界检测，即使超界也可达到 trie 树叶节点。
        而若能达到叶节点，说明在超界之前已经完成所有匹配
        """
        if trie.get("final"):
            # 如果当前走到了叶节点，将 word 添加到 结果 res 中
            res.append(trie["final"])
            trie["final"] = None    # 设置叶节点为 None，防止重复添加
            return
        if i < 0 or i == m or j < 0 or j == n:
            # 判断越界
            return
        if board[i][j] not in trie.keys():
            # 如果在 trie 树当前层中找不到当前字母，trie 树遍历终止
            return
        di, dj = [1, -1, 0, 0], [0, 0, 1, -1]
        char, board[i][j] = board[i][j], '#' # 保存当前状态，置当前状态为 visited
        for direction in range(4):
            self._dfs(board, i + di[direction], j + dj[direction], m, n, trie[char], res)
            # ii, jj = i + di[direction], j + dj[direction]
            # if ii >= 0 and ii < m and jj >= 0 and jj < n:  
            #     self._dfs(board, ii, jj, m, n, trie[char], res) # trie[char] 进入 trie 树下一层
        board[i][j] = char  # 当前分支结束，回复当前状态 unvisited

    def _build_trie(self, words):
        trie = {}
        for word in words:
            foucs = trie
            for char in word:
                foucs = foucs.setdefault(char, {})
            foucs["final"] = word
        # print(trie)
        return trie

    def test(self):
        words = ["aa"]
        board = [["a"]]
        print(self.find_words(board, words))


Solution().test()