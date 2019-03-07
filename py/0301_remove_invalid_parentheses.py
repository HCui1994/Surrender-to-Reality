"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]

Example 2:
Input: "(a)())()"
Output: ["(a)()()", "(a())()"]

Example 3:
Input: ")("
Output: [""]
"""


class Solution(object):
    def remove_invalid_parentheses(self, string):
        self.res = []
        left, right = self.count_invalid_parentheses(string)
        self.dfs(string, 0, left, right)
        return self.res

    def count_invalid_parentheses(self, parentheses):
        left = right = 0
        for p in parentheses:
            if p == '(':
                left += 1
            if p == ')':
                if left != 0:
                    left -= 1
                else:
                    right += 1
        return left, right

    def is_valid(self, parentheses):
        left, right = self.count_invalid_parentheses(parentheses)
        return left == 0 and right == 0

    def dfs(self, parentheses, start, invalid_left, invalid_right):
        if invalid_left == invalid_right and self.is_valid(parentheses):
            self.res.append(parentheses)
            return
        for i in range(start, len(parentheses)):
            if i != start and parentheses[i] == parentheses[i - 1]:
                continue
            if parentheses[i] in "()":
                if invalid_right > 0:
                    self.dfs(parentheses[:i] + parentheses[i + 1:], i,  invalid_left, invalid_right - 1)
                elif invalid_left > 0:
                    self.dfs(parentheses[:i] + parentheses[i + 1:], i, invalid_left - 1, invalid_right)

    def test(self):
        string = ")("
        self.remove_invalid_parentheses(string)
        print(self.res)


Solution().test()
