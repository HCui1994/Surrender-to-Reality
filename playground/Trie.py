class TrieUtil(object):
    @staticmethod
    def build_trie(words):
        trie = {}
        for word in words:
            curr = trie
            for c in word:
                curr = curr.setdefault(c, {})
            curr["is_leaf"] = True
        return trie
                

if __name__ == "__main__":
    trie = TrieUtil.build_trie(["a", "ab"])
    print(trie)
    TrieUtil.pretty_print_trie(trie)