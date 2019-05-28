class AnagramsUtil(object):
    def group(self, words):
        import collections

        def _encode(word):
            encoding = [0] * 26
            for char in word:
                encoding[ord(char) - ord('a')] += 1
            return tuple(encoding)

        counter = collections.defaultdict(list)
        for word in words:
            counter[_encode(word)].append(word)
        
        return [l for _, l in counter.items()]