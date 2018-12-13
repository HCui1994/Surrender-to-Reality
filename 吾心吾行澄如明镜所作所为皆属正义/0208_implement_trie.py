"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true

Note:
1.  You may assume that all inputs are consist of lowercase letters a-z.
2.  All inputs are guaranteed to be non-empty strings.

"""

class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._trie = {}
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        focus = self._trie
        for char in word:
            focus = focus.setdefault(char, {})
        focus["final"] = word        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        focus = self._trie
        for char in word:
            if focus.get(char):
                focus = focus[char]
            else:
                return False
        if focus.get("final"):
            return True
        return False
            

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        focus = self._trie
        for char in word:
            if focus.get(char):
                focus = focus[char]
            else:
                return False
        return True
        
