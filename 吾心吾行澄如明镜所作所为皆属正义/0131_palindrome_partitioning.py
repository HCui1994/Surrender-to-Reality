"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

class Solution(object):
    def partition(self, string):
        self.res = []
        self.dfs(string, [])
        print(self.res)

    def is_palindrome(self, string):
        for idx in range(len(string) // 2):
            if string[idx] != string[len(string) - 1 - idx]:
                return False
        return True

    def dfs(self, string, res):
        print(string)
        if not string:
            self.res.append(res)
            return
        for idx in range(1, len(string) + 1):
            if self.is_palindrome(string[:idx]):
                self.dfs(string[idx:], res + [string[:idx]])

    def test(self):
        string = "efe"
        self.partition(string)


Solution().test()
        
