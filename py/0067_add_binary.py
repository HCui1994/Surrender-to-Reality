"""
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.
Example 1:
Input: a = "11", b = "1"
Output: "100"
Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution(object):
    def add_binary(self, a, b):
        a, b = list(a), list(b)
        carry = 0
        res = ""
        while a and b:
            print(a, b, res)
            add = int(a[-1]) + int(b[-1]) + carry
            if add == 0:
                res = "0" + res
                carry = 0
            elif add == 1:
                res = "1" + res
                carry = 0
            elif add == 2:
                res = "0" + res
                carry = 1
            elif add == 3:
                res = "1" + res
                carry = 1
            a.pop()
            b.pop()
        
        if a:
            remain = a
        else:
            remain = b
        print(res, remain, carry)
        while remain:
            add = int(remain[-1]) + carry
            if add == 0:
                res = "0" + res
                carry = 0
            elif add == 1:
                res = "1" + res
                carry = 0
            elif add == 2:
                res = "0" + res
                carry = 1
            remain.pop()
        if carry:
            res = "1" + res
        return res

    def test(self):
        a = "11"
        b = "1"
        print(self.add_binary(a, b))


Solution().test()
            
