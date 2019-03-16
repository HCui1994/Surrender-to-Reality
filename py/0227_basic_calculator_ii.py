"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""


class Solution(object):
    """
    使用调度场算法，直接计算中缀表达式
    """

    def calculate(self, expr):

        def _calc(op, a, b):
            if op == '+':
                return a + b
            if op == '-':
                return a - b
            if op == '*':
                return a * b
            if op == '/':
                return a // b

        operator_precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
        }

        operator_stack = []
        operand_stack = []

        i = 0
        while i < len(expr):
            if expr[i] == ' ':  # skip empty spaces
                i += 1
            elif expr[i] in "1234567890":  # if token is operand
                operand = ""
                while i < len(expr) and expr[i] in "1234567890":
                    operand += expr[i]
                    i += 1
                operand_stack.append(int(operand))   # directly push stack
            elif expr[i] in "+-*/":     # if token is operator
                while operator_stack and \
                    operator_stack[-1] != '(' and \
                    operator_precedence[operator_stack[-1]] >= operator_precedence[expr[i]]:
                    operand1 = operand_stack.pop()
                    operand2 = operand_stack.pop()
                    operator = operator_stack.pop()
                    operand_stack.append(_calc(operator, operand1, operand2))
                operator_stack.append(expr[i])
                i += 1
            elif expr[i] == '(':
                operator_stack.append('(')
            elif expr[i] == ')':
                while operator_stack and operator_stack[-1] != '(':
                    operand1 = operand_stack.pop()
                    operand2 = operand_stack.pop()
                    operator = operator_stack.pop()
                    operand_stack.append(_calc(operator, operand1, operand2))
                operator_stack.pop()
        
        while operator_stack:
            operand1 = operand_stack.pop()
            operand2 = operand_stack.pop()
            operator = operator_stack.pop()
            operand_stack.append(_calc(operator, operand1, operand2))

        return operand_stack.pop()
