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
        用字典树深度限制遍历深度
        """
        print(trie, board[i][j])
        if trie.get("final"):
            res.append(trie["final"])
            trie["final"] = None        # 防止 duplicate
        if board[i][j] not in trie.keys():
            return
        di = [-1, 1, 0, 0]
        dj = [0, 0, 1, -1]
        char, board[i][j] = board[i][j], '#'  # 保存当前状态，以便在结束分支时还原状态，设置当前分支已访问
        for direction in range(4):
            ii = i + di[direction]
            jj = j + dj[direction]
            if ii >= 0 and ii < m and jj >= 0 and jj < n and board[ii][jj]:
                self._dfs(board, ii, jj, m, n, trie[char], res)
        board[i][j] = char
    
    def _build_trie(self, words):
        trie = {}   # 设置 trie 树根节点引用，防止丢失
        for word in words:
            cur = trie
            for char in word:
                cur = cur.setdefault(char, {})
            cur['final'] = word
        print(trie)
        return trie

    def test(self):
        words = ["oath","pea","eat","rain"]
        board =[['o','a','a','n'],
                ['e','t','a','e'],
                ['i','h','k','r'],
                ['i','f','l','v']
        ]
        print(self.find_words(board, words))


Solution().test()
