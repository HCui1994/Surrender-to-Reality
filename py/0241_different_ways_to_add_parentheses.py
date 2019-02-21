"""
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. 
The valid operators are +, - and *.

Example 1:
Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2

Example 2:
Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
"""


class Solution(object):
    def diff_ways_to_compute(self, string):
        return list(self.divider(string))

    def divider(self, string):
        try:
            return [int(string)]
        except ValueError:
            res = []
            for idx, symbol in enumerate(string):
                if symbol in ['*', '+', '-']:
                    left_res = self.divider(string[:idx])
                    right_res = self.divider(string[idx + 1:])
                    for left in left_res:
                        for right in right_res:
                            if symbol == '+':
                                res.append(left + right)
                            elif symbol == '-':
                                res.append(left - right)
                            else:
                                res.append(left * right)
            return res


    def test(self):
        string = "2*3-4*5"
        print(self.diff_ways_to_compute(string))
        


Solution().test()