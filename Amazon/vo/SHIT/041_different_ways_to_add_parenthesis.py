class AddParen(object):
    def diff_ways(self, expr):
        try:
            return int(expr)
        except:
            res = []
            for i, char in expr:
                if char in "+-*/":
                    left_operands = self.diff_ways(expr[:i])
                    right_operands = self.diff_ways(expr[i + 1:])
                    for operand1 in left_operands:
                        for operand2 in right_operands:
                            if char == '+':
                                res.append(operand1 + operand2)
                            elif char == '-':
                                res.append(operand1 - operand2)
                            elif char == '*':
                                res.append(operand1 * operand2)
            return res