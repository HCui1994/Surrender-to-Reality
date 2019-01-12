"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"
Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution(object):
    def adder(self, string1, string2):
        if string1 == "0":
            return string2
        if string2 == "0":
            return string1
        string1, string2 = list(string1), list(string2)
        carry, res = 0, ""
        while string1 and string2:
            add = int(string1[-1]) + int(string2[-1]) + carry
            res = str(add % 10) + res
            carry = add // 10
            string1.pop()
            string2.pop()
        remain = string1 if string1 else string2
        while remain:
            add = int(remain[-1]) + carry
            res = str(add % 10) + res
            carry = add // 10
            remain.pop()
        if carry:
            res = str(carry) + res
        return res


    def one_bit_multplier(self, string, digit):
        if digit == "0" or string == "0":
            return "0"
        if digit == "1":
            return string
        if string == "1":
            return digit
        string = list(string)
        length = 0
        res = "0"
        while string:
            res = self.adder(str(int(string[-1]) * int(digit)) + "0"*length, res)
            length += 1
            string.pop()
        return res

    def multiply(self, string1, string2):
        if string1 == "0" or string2 == "0":
            return "0"
        if string1 == "1":
            return string2
        if string2 == "1":
            return string1
        if len(string1) < len(string2):
            string1, string2 = string2, string1
        string2 = list(string2)
        res = "0"
        length = 0
        while string2:
            res = self.adder(self.one_bit_multplier(string1, string2[-1]) + "0" * length, res)
            length += 1
            string2.pop()
        return res


    def test(self):
        num1 = "123"
        num2 = "456"
        print(self.multiply(num1, num2))
    


Solution().test()

    