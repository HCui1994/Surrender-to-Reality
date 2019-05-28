class Solution:
    def mostCommonWord(self, paragraph: str, banned: [str]) -> str:
        import collections
        most_common_words = set()
        max_freq = -float("inf")
        counter = collections.Counter()

        i = 0
        while i < len(paragraph):
            if paragraph[i].lower() in "qwertyuiopasdfghjklzxcvbnm":
                activate = True
                start = i
                while i < len(paragraph) and paragraph[i].lower() in "qwertyuiopasdfghjklzxcvbnm":
                    i += 1
                word = paragraph[start: i].lower()
                if word in banned:
                    continue
                counter[word] += 1
                freq = counter[word]
                if freq > max_freq:
                    max_freq = freq
                    most_common_words = set([word])
                elif freq == max_freq:
                    most_common_words.add(word)
            else:
                i += 1
        return next(iter(most_common_words))


Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",
                          ["hit"])
