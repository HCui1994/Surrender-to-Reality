"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.
"""
import numpy as np
class Solution:
    def count_palindromic_substrings_brutal(self, s):
        """ Brutal, TLE """
        count = len(s)
        for i in range(len(s) - 1):
            for j in range(i + 2, len(s) + 1, +1):
                if self._is_palindrome(s[i: j]):
                    count += 1
        return count
    
    def _is_palindrome(self, string):
        stack = list(string[:len(string) // 2])
        if len(string) % 2:
            start = len(string) // 2 + 1
        else:
            start = len(string) // 2
        for i in range(start, len(string), +1):
            if string[i] == stack[-1]:
                stack.pop()
        if not stack:
            return True
        else:
            return False

    def count_palindromic_substrings_dp(self, s):
        """ 如果string[i:j]是回文串，且string[i-1] == string[j] 则string[i-1:j+1]也是回文串 """
        length = len(s)
        memo = [[0 for _ in range(length)] for _ in range(length)]
        for i in range(length):
            memo[i][i] = 1
        # print(np.array(memo))
        for i in range(length - 1):
            if s[i] == s[i + 1]:
                memo[i][i + 1] = 1
        # print(np.array(memo))
        for l in range(3, length + 1, +1):
            for i in range(length):
                j = i + l - 1
                print(i, j, l)
                if j >= length:
                    break
                elif s[i] == s[j] and memo[i + 1][j - 1]:
                    memo[i][j] = 1
        # print(np.array(memo))
        sum = 0
        for row in memo:
            for element in row:
                if element:
                    sum += 1
        return sum
                

    def test(self):
        string = "aaaaa"
        ans = self.count_palindromic_substring_center_check(string)
        print(ans)


soln = Solution()
soln.test()
