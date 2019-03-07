class Solution(object):
    def longest_palindromic_substring(self, string):
        """
        最长回文子串
        """
        import numpy as np
        if not string:
            return 0
        string_len = len(string)
        dp = [[0 for _ in range(string_len + 1)] for _ in range(string_len)]
        for i in range(string_len):
            dp[i][i + 1] = 1
        max_length = 1
        max_left, max_right = 0, 1
        for length in range(2, string_len + 1):
            for left in range(string_len - length + 1):
                right = left + length
                print(string_len, left, right, string[left], string[right - 1])
                if string[left] == string[right - 1] and (dp[left + 1][right - 1] or left + 2 == right):
                    dp[left][right] = dp[left + 1][right - 1] + 2
                    if dp[left][right] > max_length:
                        max_left, max_right = left, right
        print(np.array(dp))
        print(string[max_left: max_right])

    def mostCommonWord(self, paragraph, banned):
        """
        给定一个段落和一组限定词，返回最频繁的非限定单词。已知至少有一个单词是非限定的，并且答案唯一。
        限定词都是以小写字母给出，段落中的单词大小写不敏感。结果请返回小写字母。
        """
        import re
        import collections
        ban = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        print(words)
        counter = collections.Counter(w for w in words if w not in ban).most_common()
        print(counter)

    def highFive(self, results):
        import heapq
        import collections
        student_dict = collections.defaultdict(list)
        for result in results:
            sid = result.id
            score = result.score
            heapq.heappush(student_dict[sid], score)
            if len(student_dict[sid]) > 5:
                heapq.heappop(student_dict[sid])
        for sid in student_dict:
            student_dict[sid] = sum(student_dict[sid]) / 5.
        return student_dict
        

    def test(self):
        string = "abcdzdcab"
        # self.longest_palindromic_substring(string)
        self.mostCommonWord("ausdhfdsyf89ysad 8dsafys8df  asdfidsahfdahsufhdf d f f f ff d fadfdf a dsf dsa f", "d")


Solution().test()
