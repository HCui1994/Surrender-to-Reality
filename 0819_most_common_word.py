import re
import time
class Solution:
    def mostCommonWord(self, paragraph, banned):
        paragraph = paragraph.lower()
        banned = set(banned)
        words = re.split(r"[!?',;. ]", paragraph)
        dict = {}
        for word in words:
            print(dict)
            time.sleep(0.2)
            if word not in banned and word != "":
                if word in dict.keys():
                    dict[word] += 1
                else:
                    dict[word] = 1
        def key(element):
            return dict[element]
        
        return max(dict, key=key)


solution = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(solution.mostCommonWord(paragraph, banned))