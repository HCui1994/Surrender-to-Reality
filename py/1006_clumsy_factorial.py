class Solution:
    def clumsy(self, n: int) -> int:
        op_seq = ['*', '/', '+', '-']
        ops_rule = {'+': 1, '-': 1, '*': 2, '/': 2}
        expression = []
        ops = []
        i = 0
        for operand in range(n, 0, -1):
            expression.append(operand)
            if operand == 1:
                break
            operator = op_seq[i % 4]
            i += 1
            while len(ops) >= 0:
                if len(ops) == 0:
                    ops.append(operator)
                    break
                op = ops.pop()
                if op == '(' or ops_rule[operator] > ops_rule[op]:
                    ops.append(op)
                    ops.append(operator)
                    break
                else:
                    expression.append(op)
        while len(ops) > 0:
            expression.append(ops.pop())

        def _cal(n1, n2, op):
            if op == '+':
                return n1 + n2
            if op == '-':
                return n1 - n2
            if op == '*':
                return n1 * n2
            if op == '/':
                return n1 // n2

        print(expression)
        operand_stack = []
        for item in expression:
            if type(item) == str:
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                operand_stack.append(_cal(operand1, operand2, item))
            else:
                operand_stack.append(item)
        return operand_stack[0]


soln = Solution()
print(soln.clumsy(5))
