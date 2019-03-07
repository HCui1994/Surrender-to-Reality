"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:
Input: "1 + 1"
Output: 2

Example 2:
Input: " 2-1 + 2 "
Output: 3

Example 3:
Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23

Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""


class Solution(object):
    def calculator(self, string):
        self.expr = string.replace(' ', '')
        self.idx = 0
        return self.expression()

    def expression(self):
        expr = 0
        sign = True
        while self.idx < len(self.expr):
            if self.expr[self.idx] in "1234567890":
                num = ""
                while self.idx < len(self.expr) and self.expr[self.idx] in "1234567890":
                    num += self.expr[self.idx]
                    self.idx += 1
                expr += int(num) if sign else -int(num)
            elif self.expr[self.idx] in '+-':
                sign = self.expr[self.idx] == '+'
                self.idx += 1
            elif self.expr[self.idx] == '(':
                self.idx += 1
                num = self.expression()
                expr += int(num) if sign else -int(num)
            elif self.expr[self.idx] == ')':
                self.idx += 1
                break
        return expr

    def test(self):
        string = " ( 1+ ( 4 +5+ 2)- 3)+( 6  + 8) "
        print(self.calculator(string))


Solution().test()
