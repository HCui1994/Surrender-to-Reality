"""
Given a string that contains only digits 0-9 and a target value, 
    return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"] 
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []
"""


class Solution(object):
    def add_operators(self, string, target):
        if not string:
            return []
        self.target = target
        self.res = []
        if string[0] == '0':
            idx = 1
            self.operator_adder(string=string[idx:],
                                    prev_num=int(string[:idx]),
                                    prev_res=int(string[:idx]),
                                    prev_sol=string[:idx])
        else:
            for idx in range(1, len(string) + 1):
                self.operator_adder(string=string[idx:],
                                    prev_num=int(string[:idx]),
                                    prev_res=int(string[:idx]),
                                    prev_sol=string[:idx])
        print(self.res)

    def operator_adder(self, string, prev_num, prev_res, prev_sol):
        
        if not string:
            
            if prev_res == self.target:
                print(prev_sol, prev_res)
                self.res.append(prev_sol)
            return 
        if string[0] == '0':
            idx = 1
            # 加法
            self.operator_adder(string=string[idx:],
                                    prev_num=int(string[:idx]),
                                    prev_res=prev_res + int(string[:idx]),
                                    prev_sol=prev_sol + "+" + string[:idx])
            # 减法
            self.operator_adder(string=string[idx:],
                                prev_num=int(string[:idx]),
                                prev_res=prev_res - int(string[:idx]),
                                prev_sol=prev_sol + "-" + string[:idx])
            # 乘法
            self.operator_adder(string=string[idx:],
                                prev_num=prev_num * int(string[:idx]),
                                prev_res=prev_res - prev_num +
                                prev_num * int(string[:idx]),
                                prev_sol=prev_sol + "*" + string[:idx])
        else:
            for idx in range(1, len(string) + 1):
                # print(string, idx, string[:idx])
                # 加法
                self.operator_adder(string=string[idx:],
                                    prev_num=int(string[:idx]),
                                    prev_res=prev_res + int(string[:idx]),
                                    prev_sol=prev_sol + "+" + string[:idx])
                # 减法
                self.operator_adder(string=string[idx:],
                                    prev_num=-int(string[:idx]),
                                    prev_res=prev_res + (-int(string[:idx])),
                                    prev_sol=prev_sol + "-" + string[:idx])
                # 乘法
                self.operator_adder(string=string[idx:],
                                    prev_num=prev_num * int(string[:idx]),
                                    prev_res=prev_res - prev_num +
                                    prev_num * int(string[:idx]),
                                    prev_sol=prev_sol + "*" + string[:idx])

    def test(self):
        num = "3456237490"
        target = 9191
        self.add_operators(num, target)


Solution().test()
