class Brutal(object):

    def wordBreak(self, s, wordDict):
        self._string = s
        self._word_set = set(wordDict)
        return self._word_breaker(self._string)

    def _word_breaker(self, string):
        print(string)
        match_flag = False
        if string in self._word_set:
            match_flag = True
        else:
            for word in self._word_set:
                word_length = len(word)
                if word == string[:word_length]:
                    match_flag = match_flag or self._word_breaker(string[word_length:])
        
        return match_flag



class Memoization(object): # recursive dynamic programming?

    def wordBreak(self, s, wordDict):
        self._memo = [None for _ in range(len(s))]
        self._word_set = set(wordDict)
        result = self._word_breaker(string=s, position=0)
        print(self._memo)

    def _word_breaker(self, string, position):
        print(string)
        print(self._memo)
        if string == "":
            return True
        elif self._memo[position] is not None:
            return self._memo[position]
        else:
            for i in range(1, len(string), +1):
                if string[:i] in self._word_set and self._word_breaker(string[i:], position+i):
                    print("shitshitshithis")
                    self._memo[position] = True
                    return self._memo[position]
            self._memo[position] = False
            return self._memo






s = "catandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
memoization = Memoization()
print(memoization.wordBreak(s, wordDict))
