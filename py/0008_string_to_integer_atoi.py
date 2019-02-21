"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. 
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
"""

class Solution:
    def myAtoi(self, string):
        res = 0
        status = "skip"
        sign = True
        digits = set(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        for i in range(len(string)):
            if status == "skip":
                if string[i] == ' ':
                    pass
                elif string[i] == '-':
                    sign = False
                    status = "record"
                elif string[i] == '+':
                    status = "record"
                elif string[i] in digits:
                    res = res * 10 + int(string[i])
                    status = "record"
                    if sign and res >= INT_MAX:
                        return INT_MAX
                    if not sign and -res <= INT_MIN:
                        return INT_MIN
                else:
                    status = "drop"
            elif status == "record":
                if string[i] in digits:
                    res = res * 10 + int(string[i])
                    if sign and res >= INT_MAX:
                        return INT_MAX
                    if not sign and -res <= INT_MIN:
                        return INT_MIN
                else:
                    status = "drop"
            else:
                break
        return res if sign else -res
        

    def test(self):
        string = "-010101"
        print(self.my_atoi(string))


Solution().test()
