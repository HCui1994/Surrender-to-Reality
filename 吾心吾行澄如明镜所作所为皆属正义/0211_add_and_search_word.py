"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)

search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Note:
1.  You may assume that all words are consist of lowercase letters a-z.
"""

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._trie = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        focus = self._trie
        for char in word:
            focus = focus.setdefault(char, {})
        focus.setdefault("final", word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def _dfs(trie, idx):
            
            if idx == len(word) and trie.get("final") and trie["final"] == word:
                return True
            char = word[idx]
            if char != '.' and char in trie:
                return _dfs(trie[char], idx + 1)
            else:
                valid = False
                for char in trie.keys():
                    valid = valid or _dfs(trie[char], idx + 1)
                    if valid:
                        return True
                return False
        
        return _dfs(self._trie, 0)

        