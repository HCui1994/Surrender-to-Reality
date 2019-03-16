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
    """
    类似于词法分析 + 语法分析过程结合
    从左到右扫描整个串，遇到括号产生递归，递归调用返回括号内表达式的值
    """

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


class Solution2(object):
    """
    通用解法（加减，乘除需要额外添加功能，但很容易实现）
    先词法分析得到infix tokens
    再将 infix tokens 转换为 postfix tokens （调度场算法）
    再对 postfix 表达式求值
    由于相当于跑了三遍，略慢
    """

    def calculator(self, infix_expr):
        infix_tokens = self.tokenize(infix_expr)
        postfix_tokens = self.infix_to_postfix(infix_tokens)
        return self.postfix_calc(postfix_tokens)

    def tokenize(self, infix_expr):
        tokens = []
        i = 0
        while i < len(infix_expr):
            if infix_expr[i] == ' ':
                i += 1
            elif infix_expr[i] in "+-()":
                tokens.append(infix_expr[i])
                i += 1
            elif infix_expr[i] in "1234567890":
                num = ""
                while i < len(infix_expr) and infix_expr[i] in "1234567890":
                    num += infix_expr[i]
                    i += 1
                tokens.append(int(num))
        return tokens

    def infix_to_postfix(self, infix_tokens):
        postfix_tokens = []
        ops_stack = []
        for token in infix_tokens:
            if type(token) == int:
                postfix_tokens.append(token)
            elif token in "+-":
                while ops_stack and ops_stack[-1] != '(':
                    postfix_tokens.append(ops_stack.pop())
                ops_stack.append(token)
            elif token == '(':
                ops_stack.append(token)
            elif token == ')':
                while ops_stack and ops_stack[-1] != '(':
                    postfix_tokens.append(ops_stack.pop())
                ops_stack.pop()
        while ops_stack:
            postfix_tokens.append(ops_stack.pop())
        return postfix_tokens

    def postfix_calc(self, postfix_tokens):

        def _calc(op, a, b):
            if op == '+':
                return a + b
            if op == '-':
                return a - b

        stack = []
        for token in postfix_tokens:
            if type(token) == int:
                stack.append(token)
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(_calc(token, a, b))

        return stack[-1]


class Solution3(object):
    """
    添加乘除法（不同优先级）运算
    """

    def calculate(self, infix_expr):
        return self.postfix_calc(self.infix_to_postfix(self.tokenize(infix_expr)))

    def tokenize(self, infix_expr):
        """tokennize 过程不变"""
        tokens = []
        i = 0
        while i < len(infix_expr):
            if infix_expr[i] == ' ':
                i += 1
            elif infix_expr[i] in "+-*/()":
                tokens.append(infix_expr[i])
                i += 1
            elif infix_expr[i] in "1234567890":
                num = ""
                while i < len(infix_expr) and infix_expr[i] in "1234567890":
                    num += infix_expr[i]
                    i += 1
                tokens.append(int(num))
        return tokens

    

    def postfix_calc(self, postfix_tokens):
        """ 后缀式计算过程不变 """
        def _calc(op, a, b):
            if op == '+':
                return a + b
            if op == '-':
                return a - b
            if op == '*':
                return a * b
            if op == '/':
                return a // b

        stack = []
        for token in postfix_tokens:
            print(stack)
            if type(token) == int:
                stack.append(token)
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(_calc(token, a, b))

        return stack[-1]


print(Solution3().calculate("(2+6* 3+5- (3*14/    7 +2)* 5)+ 3"))
